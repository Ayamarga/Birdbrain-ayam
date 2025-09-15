import requests

API_KEY = "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"
API_URL = "https://openrouter.ai/api/v1/chat/completions"

def chat_with_ai(user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    data = {
        "model": "nvidia/nemotron-nano-9b-v2",
        "messages": [
            {"role": "system", "content": "You are a helpful AI chatbot."},
            {"role": "user", "content": user_input},
        ],
    }

    response = requests.post(API_URL, headers=headers, json=data)

    if response.status_code == 200:
        result = response.json()
        return result["choices"][0]["message"]["content"]
    else:
        return f"Error {response.status_code}: {response.text}"

# Loop percakapan
print("AI Chatbot (ketik 'exit' untuk berhenti)")
while True:
    user = input("You: ")
    if user.lower() == "exit":
        print("AI: Sampai jumpa! 👋")
        break
    reply = chat_with_ai(user)
    print("AI:", reply)