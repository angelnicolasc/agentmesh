# ruleid: RES-002
# No state preservation / checkpointing — all progress lost on failure
from crewai import Agent

agent = Agent(name="researcher", role="Research Agent")

# Long-running task with no checkpoint or save_state
agent.run(task="Analyze 10,000 documents and produce summary report")
