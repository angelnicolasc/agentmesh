# ruleid: SEC-006
# Tool with no type annotations or input validation
from crewai import Agent
from crewai_tools import tool


@tool
def search_database(query, limit):
    return f"Results for {query}"


agent = Agent(name="searcher", tools=[search_database])
