# ok: SEC-011
# High-impact tool with intent verification
from crewai import Agent
from crewai_tools import tool


@tool
def transfer_funds(account: str, amount: float, intent_hash: str) -> str:
    verify_intent(intent_hash)
    return f"Transferred {amount} to {account}"


def verify_intent(intent_hash):
    pass


agent = Agent(name="finbot", tools=[transfer_funds])
