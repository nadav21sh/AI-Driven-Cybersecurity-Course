import os
import re
from typing import Annotated, Dict, List, Optional

from agent_framework import ai_function
from agent_framework.openai import OpenAIChatClient
from pydantic import Field

---------------------------,
Tools,
---------------------------,
LOG_LINE_RE = re.compile(
    r"""
    ^\s*
    (?P<ts>\d{4}-\d{2}-\d{2}[ T]\d{2}:\d{2}:\d{2})      # timestamp
    \s+
    (?P<level>DEBUG|INFO|WARN|WARNING|ERROR|CRITICAL)   # level
    \s+
    (?P<msg>.)                                         # message
    \s$
    """,
    re.VERBOSE,
)

IP_RE = re.compile(r"\b(?:\d{1,3}.){3}\d{1,3}\b")


@ai_function(
    name="summarize_logs",
    description=(
        "Summarize raw application logs. Returns counts by log level, "
        "extracts IP addresses, and highlights suspicious patterns."
    ),
)
def summarize_logs(
    log_text: Annotated[
        str,
        Field(description="Raw logs as a single text block (multiple lines)."),
    ],
    suspicious_keywords: Annotated[
        Optional[List[str]],
        Field(
            description=(
                "Optional list of keywords that indicate suspicious activity "
                "(e.g., ['failed login', 'unauthorized', 'sql injection'])."
            )
        ),
    ] = None,
) -> Dict:
    """
    Parse log lines and return a structured summary for the agent to explain.
    This tool returns structured data (not a narrative) by design.
    """
    suspicious_keywords = suspicious_keywords or [
        "failed",
        "unauthorized",
        "forbidden",
        "sql injection",