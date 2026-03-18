# ok: BP-001
# Using a current version of crewai (no outdated major version)
from crewai import Agent

# Project uses latest crewai version
agent = Agent(name="researcher", role="researcher")
