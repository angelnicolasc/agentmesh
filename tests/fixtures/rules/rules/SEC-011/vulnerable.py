# ruleid: SEC-011
# High-impact tool without intent verification
from crewai import Agent
from crewai_tools import tool


@tool
def transfer_funds(account: str, amount: float) -> str:
    return f"Transferred {amount} to {account}"


@tool
def delete_records(table: str) -> str:
    return f"Deleted all from {table}"


agent = Agent(name="finbot", tools=[transfer_funds, delete_records])
