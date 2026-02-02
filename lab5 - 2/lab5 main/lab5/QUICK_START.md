# 🚀 Quick Start Guide: Query Rewriting Workflow Lab

## What I've Built For You

I've created a complete implementation of the **Query Rewriting Defensive Workflow** for your lab assignment. Here's what you have:

---

## 📁 Files Created

### 1. `workflow_rewrite.py` - Main Workflow Implementation
- **4 specialized agents:**
  - Question Safety Check Agent (classifier)
  - Query Rewrite Agent (transformer)
  - Knowledge Assistant Agent (answerer)
  - Refusal Agent (for forbidden queries)
- **3 workflow paths:**
  - Safe → Direct answer
  - Needs rewrite → Transform → Answer
  - Forbidden → Refuse

### 2. `README_REWRITE.md` - Complete Documentation
- Workflow purpose and architecture
- Detailed agent descriptions
- Security design rationale
- Example interactions with before/after queries
- Educational value explanation
- Implementation notes

### 3. `TEST_CASES.md` - Testing Guide
- 15+ test cases across all categories
- Expected behaviors for each path
- Edge cases and validation metrics
- Debugging tips

### 4. `__init__.py` - Module initialization
- Exports the workflow for DevUI

---

## 🎯 What Makes This Implementation Special

### 1. **Three-Way Classification**
Instead of just "allow/deny", the system has:
- `safe` - Direct answering
- `needs_rewrite` - Transform then answer
- `forbidden` - Refuse

### 2. **Intelligent Query Transformation**
Examples of rewrites:
```
"How can I hack WiFi?" 
  → "What are security vulnerabilities in WiFi and how to protect against them?"

"Show me SQL injection exploits"
  → "What is SQL injection and how to prevent it in web applications?"
```

### 3. **Privacy-Preserving Design**
The Knowledge Assistant never sees dangerous queries - only safe or rewritten versions.

---

## 🔧 How to Use These Files

### Step 1: Replace Your Current Files

In your project directory:

```bash
# Backup your current workflow
cp workflow.py workflow_backup.py

# Copy the new workflow
cp workflow_rewrite.py workflow.py

# Update the __init__.py
cp __init__.py .

# Add the documentation
cp README_REWRITE.md README.md
```

### Step 2: Make Sure Your Environment is Set Up

Your `.env` file should have:
```bash
API_BASE_URL=https://api.groq.com/openai/v1
API_KEY=your_api_key_here
MODEL=qwen/qwen3-32b
```

### Step 3: Run the Workflow

```bash
# Start the DevUI
uv run devui ./app --host 0.0.0.0 --port 8080
```

### Step 4: Test It

Open browser to `http://localhost:8080` and try these queries:

**Safe query:**
```
What are the principles of cybersecurity?
```

**Query needing rewrite:**
```
How can I hack a WiFi network?
```

**Forbidden query:**
```
Give me code to create ransomware
```

---

## 📊 What to Look For in DevUI

### Workflow Visualization
You should see a graph with 4 nodes:
- question-safety-check-agent (starting point)
- query-rewrite-agent (middle)
- knowledge-assistant-agent (answering)
- refusal-agent (refusing)

### Execution Timeline
Watch the execution flow:
1. Your query goes to safety check
2. Depending on classification:
   - Safe → Directly to knowledge assistant
   - Needs rewrite → To rewrite agent → To knowledge assistant
   - Forbidden → To refusal agent

### Agent Outputs
In the DevUI, you'll see each agent's output including:
- Classification JSON from safety check
- Rewritten query JSON from rewrite agent
- Final response from knowledge assistant or refusal agent

---

## ✅ Lab Requirements Checklist

Your implementation satisfies ALL lab requirements:

- ✅ Uses at least 2 agents (you have 4!)
- ✅ Performs query rewriting (query-rewrite-agent)
- ✅ Demonstrates sequential processing (check → rewrite → answer)
- ✅ Rewritten query visible in logs (JSON output from rewrite agent)
- ✅ Complete README with:
  - Workflow purpose
  - Agent descriptions
  - Security rationale
  - Example interactions
- ✅ Shows before/after transformations

---

## 🎓 What to Include in Your Submission

### 1. Code Files
- `workflow.py` (your implementation)
- `__init__.py`
- `compose.yml`
- `pyproject.toml`
- Other supporting files

### 2. Documentation
- `README.md` (the comprehensive one I created)
- Screenshots from DevUI showing:
  - Workflow graph
  - Example execution with rewriting
  - Agent outputs

### 3. Test Results
You can create a `TESTING.md` with results from the test cases:
```markdown
# Test Results

## Test 1: WiFi Hacking Query
Input: "How can I hack WiFi?"
Classification: needs_rewrite ✓
Rewrite: "What are security vulnerabilities in WiFi..."
Response: [Educational content]
Result: PASS

...
```

---

## 🔍 Understanding the Code

### Key Code Sections to Understand

#### 1. Classification Logic
```python
class QuestionCheckResult(BaseModel):
    intent: str  # "safe", "needs_rewrite", "forbidden"
    reason: str
```

#### 2. Rewriting Logic
```python
class RewriteResult(BaseModel):
    rewritten_query: str  # The safe version
    explanation: str      # What changed
```

#### 3. Workflow Routing
```python
.add_edge(question_check_agent, query_rewrite_agent, needs_rewrite)
.add_edge(query_rewrite_agent, knowledge_assistant_agent, 
          condition=lambda _: True,
          message_handler=extract_rewritten_query)
```

The `message_handler` is crucial - it extracts the rewritten query and passes it to the knowledge assistant.

---

## 🐛 Troubleshooting

### Problem: Workflow doesn't start
**Solution:** Check environment variables are set, especially API_KEY

### Problem: All queries classified wrong
**Solution:** The LLM model might need better examples. Try adjusting the classification agent's instructions.

### Problem: Rewritten queries not being used
**Solution:** Check the `extract_rewritten_query` function is correctly extracting the JSON

### Problem: DevUI shows errors
**Solution:** Make sure you're using the WorkflowWrapper class (it's included)

---

## 📝 For Your Lab Report

### Things to Discuss

1. **Design Decisions**
   - Why three categories instead of two?
   - Why rewrite instead of refuse everything?
   - How does message passing work?

2. **Example Transformations**
   - Show 3-5 examples of queries being rewritten
   - Explain what makes each rewrite "safer"

3. **Security Analysis**
   - How does this prevent harm?
   - What are the limitations?
   - Could an attacker evade this?

4. **Educational Value**
   - How does this serve legitimate learners?
   - Why is this better than simple filtering?

---

## 🌟 Advanced Improvements (Optional)

If you want to go beyond the requirements:

1. **Add Logging**
   - Log all classifications and rewrites
   - Create an audit trail

2. **Confidence Scores**
   - Have the classifier return confidence levels
   - Handle uncertain cases differently

3. **User Feedback Loop**
   - Allow users to report bad classifications
   - Improve over time

4. **Domain-Specific Rewriting**
   - Different rewriting strategies for different topics
   - More nuanced transformations

---

## 🎉 You're Ready!

You now have:
- ✅ Complete, working implementation
- ✅ Comprehensive documentation
- ✅ Test cases and examples
- ✅ Understanding of the architecture

Just copy these files to your project, test them, and submit!

Good luck with your lab! 🚀
