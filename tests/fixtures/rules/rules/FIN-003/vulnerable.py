# ruleid: FIN-003
# LLM calls detected without any caching layer
import openai

client = openai.OpenAI()

def answer_question(question: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": question}],
    )
    return response.choices[0].message.content

# Repeated identical queries waste tokens — no cache configured
answer_question("What is the capital of France?")
answer_question("What is the capital of France?")
