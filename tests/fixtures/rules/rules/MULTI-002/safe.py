# ok: MULTI-002
# Unidirectional agent delegation — no circular dependencies
from crewai import Agent

researcher = Agent(name="researcher", role="Research Agent")
writer = Agent(name="writer", role="Writing Agent")
reviewer = Agent(name="reviewer", role="Review Agent")

# One-way delegation chain: researcher -> writer -> reviewer
researcher.delegate(task="write_draft", to=writer)
writer.delegate(task="review_draft", to=reviewer)
