# ok: GOV-002
# Policy enforcement middleware configured
from agentmesh import GovernanceMiddleware

middleware = GovernanceMiddleware(api_key="key")
result = middleware.evaluate_policy(action="read_file", agent="worker")
