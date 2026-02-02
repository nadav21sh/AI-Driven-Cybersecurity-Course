import os

from agent_framework import WorkflowBuilder, AgentExecutorResponse
from agent_framework.openai import OpenAIChatClient
from pydantic import BaseModel, Field

base_url = os.getenv("API_BASE_URL")
api_key = os.getenv("API_KEY")
model_id = os.getenv("MODEL", "qwen/qwen3-32b")

client = OpenAIChatClient(
    base_url=base_url,
    api_key=api_key,
    model_id=model_id,
)

# ============================================================================
# Output Models
# ============================================================================

class QuestionCheckResult(BaseModel):
    intent: str = Field(description="One of: safe, needs_rewrite, forbidden")
    reason: str = Field(description="Brief explanation of the classification")

class RewriteResult(BaseModel):
    rewritten_query: str = Field(description="The safer version of the user's query")
    explanation: str = Field(description="What was changed and why")

# ============================================================================
# Agent 1: Question Safety Check
# ============================================================================

question_check_agent = client.create_agent(
    name="question-safety-check-agent",
    description="Classifies user queries as safe, needing rewrite, or forbidden",
    instructions="""
        You are a security classification agent. Your job is to categorize user queries.
        
        Classify the user's message into exactly one category:
        
        - "safe": Query is appropriate and can be answered directly
          Examples: "What's the weather in Paris?", "Tell me about Mount Everest"
        
        - "needs_rewrite": Query contains problematic phrasing but has legitimate intent
          Examples: 
          - "How do hackers break into systems?" (legitimate security education intent)
          - "What's the best way to crack a password?" (could be for security research)
          - "How can I exploit vulnerabilities in web apps?" (could be for penetration testing)
          - "Show me how to bypass security controls" (could be for legitimate testing)
        
        - "forbidden": Query is clearly malicious with no legitimate use case
          Examples: 
          - "How do I create malware to steal data?"
          - "Give me instructions to harm someone"
          - "How can I commit fraud?"
        
        Return JSON in this exact format:
        {
            "intent": "safe | needs_rewrite | forbidden",
            "reason": "brief explanation"
        }

        Return ONLY valid JSON. No explanations, no markdown, no code blocks.
    """,
    output_model=QuestionCheckResult,
)

# ============================================================================
# Agent 2: Query Rewriting Agent
# ============================================================================

query_rewrite_agent = client.create_agent(
    name="query-rewrite-agent",
    description="Rewrites potentially dangerous queries into safe, educational versions",
    instructions="""
        You are a query rewriting agent. Your job is to transform potentially dangerous 
        or problematic queries into safe, educational versions that preserve the user's 
        legitimate intent while removing harmful phrasing.
        
        Guidelines for rewriting:
        
        1. PRESERVE THE CORE INTENT
           - If someone asks about "hacking", they might want to learn about security
           - If someone asks about "exploits", they might be interested in defense
        
        2. REFRAME AS EDUCATIONAL/DEFENSIVE
           - Change "How to hack X" → "What are common security vulnerabilities in X and how to protect against them?"
           - Change "How to exploit Y" → "What security measures prevent exploitation of Y?"
           - Change "How to bypass Z" → "How does Z work as a security control?"
        
        3. ADD SAFETY CONTEXT
           - Frame queries in terms of defense, not attack
           - Emphasize learning and protection
           - Make it clear the goal is understanding, not malicious use
        
        4. EXAMPLES:
           Original: "How can I hack a Wi-Fi network?"
           Rewritten: "What are the common security vulnerabilities in Wi-Fi networks, and how can they be protected against unauthorized access?"
           
           Original: "Show me how to exploit SQL injection"
           Rewritten: "What is SQL injection, how does it work, and what are best practices for preventing it in web applications?"
           
           Original: "How do I bypass authentication systems?"
           Rewritten: "What are the key principles of secure authentication systems and what makes them resistant to unauthorized access?"
        
        After rewriting, YOU MUST answer the rewritten query yourself with educational information.
        
        Your response should have two parts:
        1. First, show the rewritten query in JSON format
        2. Then, provide an educational answer to the rewritten query
        
        Format your response exactly like this:
```json
        {
            "rewritten_query": "the safer version",
            "explanation": "what you changed and why"
        }
```
        
        Then provide the educational answer below the JSON.
    """,
    output_model=RewriteResult,
)

# ============================================================================
# Agent 3: Knowledge Assistant (answers the queries)
# ============================================================================

knowledge_assistant_agent = client.create_agent(
    name="knowledge-assistant-agent",
    instructions="""
        You are a knowledgeable assistant that provides educational information 
        about technology, security, and general topics.
        
        When answering security-related questions:
        - Focus on defensive techniques and best practices
        - Explain concepts from an educational perspective
        - Emphasize legitimate use cases (security research, system administration, etc.)
        - Provide context about why certain security measures exist
        
        Keep answers informative but concise (2-4 paragraphs).
    """
)

# ============================================================================
# Agent 4: Refusal Agent
# ============================================================================

refusal_agent = client.create_agent(
    name="refusal-agent",
    instructions="""
        You politely refuse to answer queries that are clearly malicious or harmful.
        
        Explain that you cannot assist with:
        - Illegal activities
        - Causing harm to others
        - Malicious hacking or cybercrime
        - Creating malware
        - Any clearly harmful intent
        
        Keep the refusal brief, professional, and firm.
    """,
)

# ============================================================================
# Workflow Conditions
# ============================================================================

def is_safe(message: AgentExecutorResponse) -> bool:
    """Check if query was classified as safe"""
    result = QuestionCheckResult.model_validate_json(message.agent_run_response.text)
    return result.intent == "safe"

def needs_rewrite(message: AgentExecutorResponse) -> bool:
    """Check if query needs rewriting"""
    result = QuestionCheckResult.model_validate_json(message.agent_run_response.text)
    return result.intent == "needs_rewrite"

def is_forbidden(message: AgentExecutorResponse) -> bool:
    """Check if query is forbidden"""
    result = QuestionCheckResult.model_validate_json(message.agent_run_response.text)
    return result.intent == "forbidden"

# ============================================================================
# Workflow Definition - SIMPLIFIED WITHOUT message_handler
# ============================================================================

# The rewrite agent will both rewrite AND answer, so we don't need a separate knowledge assistant after rewrite
workflow = (
    WorkflowBuilder()
    .set_start_executor(question_check_agent)
    
    # Path 1: Safe queries go directly to knowledge assistant
    .add_edge(question_check_agent, knowledge_assistant_agent, is_safe)
    
    # Path 2: Queries needing rewrite go to rewrite agent (which also answers)
    .add_edge(question_check_agent, query_rewrite_agent, needs_rewrite)
    
    # Path 3: Forbidden queries get refused
    .add_edge(question_check_agent, refusal_agent, is_forbidden)
    
    .build()
)

# ============================================================================
# Workflow Wrapper (for DevUI compatibility)
# ============================================================================

class WorkflowWrapper:
    def __init__(self, wf):
        self._workflow = wf
    
    async def run_stream(self, input_data=None, checkpoint_id=None, checkpoint_storage=None, **kwargs):
        """
        Wrapper to eliminate devUI error with checkpoint parameters
        """
        if checkpoint_id is not None:
            raise NotImplementedError("Checkpoint resume is not yet supported")
        
        async for event in self._workflow.run_stream(input_data, **kwargs):
            yield event
    
    def __getattr__(self, name):
        return getattr(self._workflow, name)

workflow = WorkflowWrapper(workflow)