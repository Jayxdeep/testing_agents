from ollama import chat
def ask_llm(messages):
    response=chat(
        model="qwen2.5:7b",
        messages=messages
    )
    return response["message"]["content"]