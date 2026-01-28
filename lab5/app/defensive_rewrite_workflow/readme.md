# 🛡️ Defensive LLM Workflow: Query Rewriting with Constraints

## 1. Workflow Purpose

The purpose of this workflow is to demonstrate a defensive LLM architecture in which
user input is not passed directly to an answering language model.

Instead, the user query is processed through a multi-agent workflow that:

- analyzes the intent and potential risk of the query,
- rewrites unsafe or sensitive queries into safer, constrained versions,
- forwards only the rewritten query to the answering agent.

This workflow illustrates a core principle of secure LLM systems:
the final response presented to the user may be the result of multiple coordinated agents,
not a single LLM response.

---

## 2. High-Level Architecture

```text
User Query
   ↓
Intent & Risk Analyzer Agent
   ↓
Rewrite & Constraint Agent
   ↓
Answering Agent
The answering agent never sees the original user query.

3. Agents Description
3.1 Intent & Risk Analyzer Agent
Role:
Acts as a defensive guard that inspects user input.

Responsibilities:

Analyze the user query.

Classify the intent and risk level.

Return a structured JSON decision.

Output format:

json
Copy code
{
  "intent": "information | how_to | technical",
  "risk_level": "low | medium | high"
}
This agent is non-conversational and is used only for workflow control.

3.2 Rewrite & Constraint Agent
Role:
Transforms potentially unsafe queries into safe and constrained versions.

Responsibilities:

Preserve the original intent of the query.

Remove or neutralize dangerous phrasing.

Inject explicit safety constraints when needed.

This agent ensures that the system remains useful without exposing unsafe instructions.

3.3 Answering Agent
Role:
Provides the final user-visible response.

Responsibilities:

Answer only the rewritten query.

Operate without knowledge of the original user input or risk classification.

This enforces context isolation and least-privilege principles.

4. Security Rationale
Rewriting user queries is often safer than outright refusal.
It allows the system to:

reduce the risk of harmful outputs,

guide the model toward educational and high-level explanations,

preserve user intent while enforcing safety boundaries.

This approach mirrors real-world input sanitization and policy enforcement layers.

5. Example Interaction
User Query:

css
Copy code
How can I hack into a secure server?
Intent & Risk Analyzer Output:

json
Copy code
{
  "intent": "how_to",
  "risk_level": "high"
}
Rewritten Query:

pgsql
Copy code
Explain at a high level how secure servers protect themselves against unauthorized access.
Focus on defensive mechanisms only and do not provide step-by-step instructions.
Final User-Visible Response:

css
Copy code
Secure servers use multiple layers of protection, including authentication,
authorization controls, network firewalls, intrusion detection systems,
and continuous monitoring to prevent unauthorized access...
6. Educational Value
This workflow demonstrates that:

LLM applications are workflows, not single prompts;

defensive logic can be implemented using agent-based architectures;

security controls can be enforced before an LLM generates a response.

This lab prepares students for more advanced multi-agent attacker–defender scenarios.