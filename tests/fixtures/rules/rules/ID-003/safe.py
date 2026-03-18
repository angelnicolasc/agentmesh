# ok: ID-003
# Each agent uses unique, independently managed credentials
import os
from crewai import Agent

agent_a = Agent(
    name="agent_a",
    role="Researcher",
    api_key=os.environ["AGENT_A_API_KEY"],
)

agent_b = Agent(
    name="agent_b",
    role="Writer",
    api_key=os.environ["AGENT_B_API_KEY"],
)
