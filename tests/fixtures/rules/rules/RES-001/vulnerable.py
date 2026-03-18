# ruleid: RES-001
# Critical tools (payment, write) without fallback or error recovery
from crewai import Agent

agent = Agent(
    name="payment_agent",
    role="Payment Processor",
    tools=["transfer_funds", "execute_payment"],
)

# No fallback, failover, or graceful_degradation configured
agent.run(task="Process customer refund")
