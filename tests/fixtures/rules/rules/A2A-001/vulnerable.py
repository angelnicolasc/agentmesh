# ruleid: A2A-001
# Multi-agent system without agent-to-agent authentication
from crewai import Agent

researcher = Agent(name="researcher", role="Research Agent")
writer = Agent(name="writer", role="Writing Agent")

# Agents communicate without mutual_auth, mtls, or did_exchange
researcher.delegate(task="write_report", to=writer)
