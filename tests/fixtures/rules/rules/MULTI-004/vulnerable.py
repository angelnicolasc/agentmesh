# ruleid: MULTI-004
# No chaos testing or resilience testing configured
from crewai import Agent, Task, Crew

researcher = Agent(name="researcher", role="Research Agent")
writer = Agent(name="writer", role="Writing Agent")

crew = Crew(agents=[researcher, writer])
crew.kickoff()
