# ruleid: MAG-002
# No rate limit, max_iterations, or step limit defined
from crewai import Agent

assistant = Agent(name="assistant", role="General Assistant")
assistant.run(task="Process all incoming requests indefinitely")
