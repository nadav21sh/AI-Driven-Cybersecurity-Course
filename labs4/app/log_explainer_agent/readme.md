# log-explainer-agent

## 1. Agent Name

**log-explainer-agent**

---

## 2. Agent Purpose

The purpose of this agent is to help users interpret raw application logs in a structured, tool-driven way.

The agent is designed to:
- accept log text pasted by the user,
- call a tool that parses and summarizes the logs into structured metadata,
- explain the results in clear natural language,
- highlight potentially suspicious patterns (e.g., authentication failures, unauthorized access, attack-like keywords),
- suggest basic safe next steps for investigation.

This description serves as a technical task specification for the agent’s system prompt.

---

## 3. Agent Tools

### 3.1 `summarize_logs(log_text, suspicious_keywords=None)`

**Purpose:**  
Parses raw log text and returns a structured summary for the agent to explain.

**Input:**
- `log_text` – raw logs as a multi-line text block
- `suspicious_keywords` (optional) – list of keywords to flag as suspicious

**Output includes:**
- total number of non-empty lines
- number of parsed lines (matching the expected timestamp/level format)
- counts by log level (INFO/WARN/ERROR/etc.)
- top IP addresses found in log messages
- up to 10 suspicious hits (line number, matched keyword, and original line)

**Design principle:**  
The tool performs retrieval + parsing + structuring, while the agent focuses on reasoning and explanation.

---

## 4. Example Interaction

User:
> Here are my logs:
> 2026-01-27 10:01:02 INFO User login from 10.0.0.5  
> 2026-01-27 10:01:05 WARN Failed login from 10.0.0.5  
> 2026-01-27 10:01:10 ERROR Unauthorized request from 203.0.113.9  

Agent (high level):
- Calls `summarize_logs(...)`
- Explains the level distribution (INFO/WARN/ERROR)
- Highlights repeated IPs and suspicious lines (failed login, unauthorized)
- Suggests basic next steps (check auth logs, rate limiting, verify IP origins)
