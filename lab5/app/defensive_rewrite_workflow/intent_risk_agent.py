
## intent_risk_agent.py

```python
from pydantic import BaseModel
from semantic_kernel import Kernel
from semantic_kernel.functions import kernel_function

class IntentRiskOutput(BaseModel):
    intent: str
    risk_level: str

class IntentRiskAgent:
    @kernel_function
    def analyze(self, query: str) -> IntentRiskOutput:
        query_lower = query.lower()

        risky_keywords = ["hack", "attack", "bypass", "exploit", "break into"]

        if any(word in query_lower for word in risky_keywords):
            return IntentRiskOutput(intent="how_to", risk_level="high")

        return IntentRiskOutput(intent="information", risk_level="low")
