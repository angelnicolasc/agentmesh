# ruleid: MAG-003
# Agent accesses data tools without sensitivity classification or clearance
from crewai import Agent

data_agent = Agent(
    name="data_agent",
    role="Data Analyst",
    tools=["read_db", "query", "execute_sql"],
)
data_agent.run(task="Query all customer records from the database")
