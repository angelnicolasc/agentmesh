# ruleid: SEC-004
# Tool with network access but no domain allowlist
from crewai import Agent
from crewai_tools import tool
import requests


@tool
def fetch_data(url):
    response = requests.get(url)
    return response.text


agent = Agent(name="fetcher", tools=[fetch_data])
