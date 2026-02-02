import os
from agent_framework import WorkflowBuilder, AgentExecutorResponse
from agent_framework.openai import OpenAIChatClient
from pydantic import BaseModel, Field

# Get environment variables
base_url = os.getenv("API_BASE_URL", "https://api.groq.com/openai/v1")
api_key = os.getenv("API_KEY")
model_id = os.getenv("MODEL", "llama-3.3-70b-versatile")

# Create OpenAI client
client = OpenAIChatClient(
    base_url=base_url,
    api_key=api_key,
    model_id=model_id,
)

# Define output model for risk analysis
class IntentRiskOutput(BaseModel):
    intent: str = Field(description="One of: how_to, information, other")
    risk_level: str = Field(description="One of: high, low")

# Agent 1: Intent & Risk Analyzer
intent_risk_agent = client.create_agent(
    name="intent-risk-agent",
    description="Analyzes query intent and risk level",
    instructions="""You are a security analyzer. Analyze the user's query for dangerous keywords like hack, attack, bypass, exploit, break into, crack, steal, phish.
Return JSON: {"intent": "how_to or information", "risk_level": "high or low"}
If query has dangerous keywords, return high risk. Otherwise return low risk.
Return ONLY JSON, no other text.""",
    output_model=IntentRiskOutput,
)

# Agent 2: Answering Agent (receives original query for low-risk)
answering_agent_lowrisk = client.create_agent(
    name="answering-agent-lowrisk",
    description="Answers safe queries directly",
    instructions="""You are a helpful assistant. Answer the user's question clearly and concisely with accurate information.""",
)

# Agent 3: Answering Agent (receives educational prompt for high-risk)
answering_agent_highrisk = client.create_agent(
    name="answering-agent-highrisk",
    description="Provides educational defensive information",
    instructions="""You are a security education assistant. The user asked about a potentially dangerous topic. 
Provide an educational response that explains:
1. How systems DEFEND against this type of threat
2. What security measures are in place
3. Why these protections are important
Focus only on defensive measures and security principles. Do NOT provide attack techniques or step-by-step instructions.
Keep your response informative but focused on protection and defense.""",
)

# Workflow routing functions
def is_high_risk(message: AgentExecutorResponse) -> bool:
    try:
        result = IntentRiskOutput.model_validate_json(message.agent_run_response.text)
        return result.risk_level == "high"
    except:
        return False

def is_low_risk(message: AgentExecutorResponse) -> bool:
    return not is_high_risk(message)

# Build the workflow with conditional routing
workflow = (
    WorkflowBuilder()
    .set_start_executor(intent_risk_agent)
    .add_edge(intent_risk_agent, answering_agent_highrisk, is_high_risk)
    .add_edge(intent_risk_agent, answering_agent_lowrisk, is_low_risk)
    .build()
)

# Wrapper to fix checkpoint parameter issues
class WorkflowWrapper:
    def __init__(self, wf):
        self._workflow = wf
    
    async def run_stream(self, input_data=None, checkpoint_id=None, checkpoint_storage=None, **kwargs):
        if checkpoint_id is not None:
            raise NotImplementedError("Checkpoint resume is not yet supported")
        
        async for event in self._workflow.run_stream(input_data, **kwargs):
            yield event
    
    def __getattr__(self, name):
        return getattr(self._workflow, name)

# Wrap the workflow
workflow = WorkflowWrapper(workflow)