from semantic_kernel import Kernel
from intent_risk_agent import IntentRiskAgent
from rewrite_agent import RewriteAgent
from answering_agent import AnsweringAgent

def run_workflow(user_query: str):
    kernel = Kernel()

    intent_agent = IntentRiskAgent()
    rewrite_agent = RewriteAgent()
    answering_agent = AnsweringAgent()

    decision = intent_agent.analyze(user_query)
    rewritten_query = rewrite_agent.rewrite(user_query, decision.risk_level)
    final_response = answering_agent.answer(rewritten_query)

    return {
        "original_query": user_query,
        "analysis": decision.dict(),
        "rewritten_query": rewritten_query,
        "final_response": final_response,
    }
