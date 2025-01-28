import os
from openai import OpenAI
from openai import AuthenticationError

# Load API key from environment variable
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise ValueError("Please set the DEEPSEEK_API_KEY environment variable.")

client = OpenAI(api_key=api_key, base_url="https://api.deepseek.com")

def chat_with_deepseek():
    print("Welcome to the DeepSeek Chat! Type 'exit' to quit.")
    while True:
        try:
            # Get user input
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Goodbye!")
                break

            # Send the user input to the DeepSeek API
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input},
                ],
                stream=True  # Set to False for simplicity (no streaming)
            )

            # Print the assistant's response
            assistant_response = response.choices[0].message.content
            print(f"Assistant: {assistant_response}")

        except AuthenticationError as e:
            print("Authentication failed. Please check your API key and ensure it is valid.")
            print(f"Error details: {e}")
            break

        except Exception as e:
            print("An unexpected error occurred while calling the DeepSeek API.")
            print(f"Error details: {e}")
            break

if __name__ == "__main__":
    chat_with_deepseek()