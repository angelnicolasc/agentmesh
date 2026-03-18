# ruleid: ODD-004
# Agents defined without any time constraints (timeout, max_iterations, etc.)
from crewai import Agent

researcher = Agent(name="researcher", role="Research Agent")
writer = Agent(name="writer", role="Writing Agent")
