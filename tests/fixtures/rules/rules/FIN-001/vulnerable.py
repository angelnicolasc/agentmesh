# ruleid: FIN-001
# LLM API calls without any cost tracking mechanism
import openai

client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Summarize this document"}],
)
# No usage/cost tracking — total_tokens, prompt_tokens not captured
print(response.choices[0].message.content)
