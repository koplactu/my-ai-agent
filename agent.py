from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve API key and base URL from environment variables
api_key = os.getenv("OPENAI_API_KEY")
base_url = os.getenv("OPENAI_BASE_URL")

# Initialize the client with the API key and base URL
client = OpenAI(api_key=api_key, base_url=base_url)

print("Chat with the AI (type 'exit' to quit)")

messages = [{"role": "system", "content": "You are a helpful assistant."}]

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        print("Exiting chat...")
        break

    messages.append({"role": "user", "content": user_input})

    completion = client.chat.completions.create(
        model="llama3:7b",
        messages=messages
    )

    response = completion.choices[0].message.content
    messages.append({"role": "assistant", "content": response})

    print(f"AI: {response}")
