# ruleid: ID-002
# No identity definition (no auth, credentials, or agent_id configuration)
from crewai import Agent

agent = Agent(name="assistant", role="Helper")
agent.run(task="Process user requests")
