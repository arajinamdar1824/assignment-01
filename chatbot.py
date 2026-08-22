print("🤖 ChatBot: Hello! I'm a simple chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")

    elif "how are you" in user:
        print("Bot: I'm doing great! 😊")

    elif "your name" in user:
        print("Bot: My name is PyBot.")

    elif "python" in user:
        print("Bot: Python is awesome! 🐍")

    elif user == "bye":
        print("Bot: Goodbye! 👋")
        break

    else:
        print("Bot: Sorry, I don't understand that yet.")
