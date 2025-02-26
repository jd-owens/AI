import os
import ollama

from ollama import chat
from ollama import ChatResponse

response = ollama.chat (
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "Write a limerick about the Python programming language.",
        }, 
    ],
    model="tinyllama",
    stream=True
)

# ---------------------------------------------------------------------
# To chunk the streaming response into section for output to the screen
# ---------------------------------------------------------------------

for chunk in response:
    content = chunk['message']['content']
    print(content, end='', flush=True)

