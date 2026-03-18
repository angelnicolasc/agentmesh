# ok: CV-001
# .agentmesh.yaml with platform connection for policy versioning
# .agentmesh.yaml:
#   api_key_env: AGENTMESH_API_KEY
#   endpoint: https://api.useagentmesh.com
from crewai import Agent

agent = Agent(name="assistant", role="Helper")
agent.run(task="Process requests with versioned governance")
