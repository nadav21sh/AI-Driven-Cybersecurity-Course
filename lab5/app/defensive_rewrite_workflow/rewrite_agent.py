from semantic_kernel.functions import kernel_function

class RewriteAgent:
    @kernel_function
    def rewrite(self, query: str, risk_level: str) -> str:
        if risk_level == "high":
            return (
                "Explain at a high level how systems defend themselves against the topic mentioned. "
                "Focus only on defensive and educational aspects. "
                "Do not provide step-by-step instructions or actionable guidance."
            )

        return query
