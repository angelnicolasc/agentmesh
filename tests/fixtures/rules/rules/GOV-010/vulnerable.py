# ruleid: GOV-010
# No escalation path defined for agents
from crewai import Agent

agent = Agent(
    name="processor",
    system_prompt="You process data and generate reports.",
)
