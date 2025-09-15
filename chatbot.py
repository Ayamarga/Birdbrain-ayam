import json
import os

# Nama file memory
MEMORY_FILE = "memory.json"

# Memory sementara di RAM
memory = {}

# Fungsi untuk load memory saat program dibuka
def load_memory():
    global memory
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, "r") as f:
            try:
                memory = json.load(f)
            except:
                memory = {}
    else:
        memory = {}

# Fungsi untuk save memory saat keluar
def save_memory():
    with open(MEMORY_FILE, "w") as f:
        json.dump(memory, f)

# Chatbot utama
def chatbot():
    load_memory()
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

# Jalankan program
if __name__ == "__main__":
    chatbot()
    
    from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Data training kecil
X = ["hi", "hello", "hey", "bye", "goodbye", "see you"]
y = ["greet", "greet", "greet", "farewell", "farewell", "farewell"]

vec = CountVectorizer()
X_vec = vec.fit_transform(X)

clf = MultinomialNB()
clf.fit(X_vec, y)

while True:
    user = input("You: ").lower()
    if user == "exit":
        print("AI: Bye! 👋")
        break

    pred = clf.predict(vec.transform([user]))[0]
    if pred == "greet":
        print("AI: Hello! 👋")
    elif pred == "farewell":
        print("AI: Goodbye! 👋")
    else:
        print("AI: I don't know yet...")