# ruleid: SEC-003
# Tool with filesystem access but no path validation
from crewai import Agent
from crewai_tools import tool


@tool
def read_document(file_path):
    with open(file_path, "r") as f:
        return f.read()


agent = Agent(name="reader", tools=[read_document])
