# ruleid: MULTI-001
# Multi-agent system without topology monitoring or observability
from crewai import Agent

researcher = Agent(name="researcher", role="Research Agent")
writer = Agent(name="writer", role="Writing Agent")
reviewer = Agent(name="reviewer", role="Review Agent")
