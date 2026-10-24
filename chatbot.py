import ollama

MODEL = "phi3"   # change to "phi3" or "mistral" if you pulled those

system_prompt = "You are a helpful, concise assistant."

messages = [{"role": "system", "content": system_prompt}]

print("Chatbot ready. Type /reset to clear, /quit to exit.\n")

while True:
    user = input("You: ").strip()
    if not user:
        continue
    if user.lower() == "/quit":
        break
    if user.lower() == "/reset":
        messages = [{"role": "system", "content": system_prompt}]
        print("(reset)\n")
        continue

    messages.append({"role": "user", "content": user})

    resp = ollama.chat(model=MODEL, messages=messages)
    assistant = resp["message"]["content"].strip()

    print(f"Bot: {assistant}\n")
    messages.append({"role": "assistant", "content": assistant})
