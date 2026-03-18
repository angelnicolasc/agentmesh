# ruleid: MULTI-003
# Multiple agents share a write tool without contention protection
from crewai import Agent

agent_a = Agent(name="agent_a", role="Writer", tools=["database_write"])
agent_b = Agent(name="agent_b", role="Editor", tools=["database_write"])

# Both agents use the same write tool concurrently with no locking
agent_a.execute(tool="database_write", args={"table": "posts", "data": "new row"})
agent_b.execute(tool="database_write", args={"table": "posts", "data": "another row"})
