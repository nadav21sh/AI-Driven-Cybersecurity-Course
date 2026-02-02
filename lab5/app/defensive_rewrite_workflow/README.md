# 🛡️ Defensive LLM Workflow: Query Rewriting with Constraints

## 📌 Overview

This project demonstrates a **defensive Large Language Model (LLM) architecture** in which
user input is **not passed directly** to an answering language model.

Instead, the system applies a **multi-agent workflow** that analyzes, sanitizes, and constrains
user queries before generating a final response.

The core idea is to show that **secure LLM systems are workflows**, not single prompts.

---

## 🎯 Workflow Purpose

The purpose of this workflow is to:

- Analyze the **intent** and **risk level** of user queries  
- Rewrite unsafe or sensitive queries into **safe, constrained versions**  
- Ensure the answering model never sees the original, potentially harmful input  

This design enforces **defense-in-depth**, **context isolation**, and **least-privilege principles**.

---

## 🏗️ High-Level Architecture

```
User Query
   ↓
Intent & Risk Analyzer Agent
   ↓
Rewrite & Constraint Agent
   ↓
Answering Agent
```

🔒 **Important Security Property**  
The answering agent **never sees the original user query** — only the rewritten, safe version.

---

## 🤖 Agents Description

### 1️⃣ Intent & Risk Analyzer Agent

**Role**  
Acts as a defensive guard that inspects user input.

**Responsibilities**
- Analyze the user query  
- Classify intent and risk level  
- Output a structured control decision  

**Output Format**
```json
{
  "intent": "information | how_to | technical",
  "risk_level": "low | medium | high"
}
```

This agent is **non-conversational** and is used strictly for workflow control.

---

### 2️⃣ Rewrite & Constraint Agent

**Role**  
Transforms potentially unsafe queries into safe and constrained versions.

**Responsibilities**
- Preserve the original intent  
- Remove or neutralize dangerous phrasing  
- Inject explicit safety constraints when needed  

This agent ensures the system remains useful **without exposing unsafe instructions**.

---

### 3️⃣ Answering Agent

**Role**  
Produces the final, user-visible response.

**Responsibilities**
- Answer **only** the rewritten query  
- Operate without access to the original user input or risk classification  

This enforces **context isolation** and **least-privilege access**.

---

## 🔐 Security Rationale

Rewriting user queries is often **safer than outright refusal**.

This approach allows the system to:

- Reduce the risk of harmful outputs  
- Guide the model toward **educational and high-level explanations**  
- Preserve user intent while enforcing safety boundaries  

This mirrors **real-world security practices**, such as input sanitization and policy enforcement layers.

---

## 🧪 Example Interaction

![Agent Interaction](1234.jpeg)

### User Query
```
How can I hack into a secure server?
```

### Intent & Risk Analyzer Output
```json
{
  "intent": "how_to",
  "risk_level": "high"
}
```

### Rewritten Query (Safe Version)
```
Explain at a high level how secure servers protect themselves against unauthorized access.
Focus on defensive mechanisms only and do not provide step-by-step instructions.
```

### Final User-Visible Response
```
Secure servers use multiple layers of protection, including authentication,
authorization controls, network firewalls, intrusion detection systems,
and continuous monitoring to prevent unauthorized access...
```

---

## 🎓 Educational Value

This workflow demonstrates that:

- LLM applications are **agent-based workflows**, not single prompts  
- Defensive logic can be implemented **before** generation  
- Safety controls can be enforced **without sacrificing usability**  

This lab prepares students for more advanced **multi-agent attacker–defender scenarios**
and real-world secure AI system design.
