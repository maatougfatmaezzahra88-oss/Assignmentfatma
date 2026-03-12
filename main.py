import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

print("Welcome! Ask me anything. Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")

    if user_input.strip().lower() == "quit":
        print("Goodbye!")
        break

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": user_input,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    response = chat_completion.choices[0].message.content
    print(f"\nAssistant: {response}\n")
