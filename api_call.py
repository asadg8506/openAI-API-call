from openai import OpenAI

client = OpenAI( api_key="API KEY HERE")

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "tell me about freelancing"}]
)

print(completion.choices[0].message.content)
