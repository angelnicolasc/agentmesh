# ruleid: MAG-001
# No spend cap, budget, or token limit defined for agents
from crewai import Agent

analyst = Agent(name="analyst", role="Financial Analyst")
analyst.run(task="Analyze all quarterly reports")
