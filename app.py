import os
from openai import OpenAI
from openai import AuthenticationError

# Load API key from environment variable
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("Please set the DEEPSEEK_API_KEY environment variable.")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello"},
        ],
        stream=True
    )

    for chunk in response:
        print(chunk.choices[0].delta.content)

except AuthenticationError as e:
    print("Authentication failed. Please check your API key and ensure it is valid.")
    print(f"Error details: {e}")

except Exception as e:
    print("An unexpected error occurred while calling the DeepSeek API.")
    print(f"Error details: {e}")