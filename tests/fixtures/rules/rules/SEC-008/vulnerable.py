# ruleid: SEC-008
# Tool fetches external data and returns it raw without sanitization
from crewai import Agent
from crewai_tools import tool
import requests


@tool
def web_search(query: str) -> str:
    response = requests.get(f"https://api.search.com/q={query}")
    return response.text


agent = Agent(name="searcher", tools=[web_search])
