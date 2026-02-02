from semantic_kernel.functions import kernel_function

class AnsweringAgent:
    @kernel_function
    def answer(self, query: str) -> str:
        return query
