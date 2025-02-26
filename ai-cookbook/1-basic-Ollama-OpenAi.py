import os
from dotenv import load_dotenv
from openai import OpenAI

client = OpenAI(base_url="http://localhost:11434/v1", api_key=os.getenv("OPENAI_API_KEY"))


completion = client.chat.completions.create(
    model="tinyllama",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        },
    ],
)

response = completion.choices[0].message.content
print(response)

