# ok: GOV-008
# Critical tool with retry logic
from crewai import Agent
from crewai_tools import tool
from tenacity import retry, stop_after_attempt, wait_exponential


@tool
@retry(stop=stop_after_attempt(3), wait=wait_exponential())
def send_email(to: str, body: str) -> str:
    return f"Email sent to {to}"


agent = Agent(name="mailer", tools=[send_email])
