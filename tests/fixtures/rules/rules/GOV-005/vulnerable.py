# ruleid: GOV-005
# No circuit breaker configured
from crewai import Agent

agent = Agent(
    name="worker",
    system_prompt="You are a helpful assistant that processes tasks.",
)
