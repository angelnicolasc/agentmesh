# ok: CV-002
# Audit logging WITH platform connection — entries include policy_snapshot_id
# .agentmesh.yaml:
#   audit:
#     enabled: true
#     log_level: verbose
#   api_key_env: AGENTMESH_API_KEY
#   endpoint: https://api.useagentmesh.com
from crewai import Agent

agent = Agent(name="assistant", role="Helper")
agent.run(task="Run audited workflow with version-tagged entries")
