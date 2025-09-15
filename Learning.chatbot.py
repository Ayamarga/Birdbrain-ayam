import json
import os

# File to store learned responses
DATA_FILE = "memory.json"

# Load existing memory or start fresh
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        memory = json.load(f)
else:
    memory = {}

def save_memory():
    with open(DATA_FILE, "w") as f:
        json.dump(memory, f)

def chatbot():
    print("Learning Chatbot 🤖 (type 'exit' to quit)")
    print("If I don’t know something, teach me!")

    while True:
        user = input("You: ").lower()
        if user == "exit":
            print("AI: Bye! 👋")
            save_memory()
            break

        if user in memory:
            print("AI:", memory[user])
        else:
            print("AI: I don’t know how to respond. What should I say?")
            reply = input("Teach me: ")
            memory[user] = reply
            print("AI: Got it! I'll remember that.")

if __name__ == "__main__":
    chatbot()