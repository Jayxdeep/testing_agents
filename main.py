from services.chat_service import ask_llm
#from services.weather_service import get_weather
from tools.weather_tool import get_weather
from memory.chat_memory import messages
from router.intent_router import is_weather_query

print("Local AI Chat Started! Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    if is_weather_query(user_input):
        #print("[Router] weather tool wokring") just to see the debug

        weather_info = get_weather()

        enhanced_prompt = f"""
User Question:
{user_input}

Weather Data:
{weather_info}
"""

        messages.append({
            "role": "user",
            "content": enhanced_prompt
        })

    else:
        #print("[router] normal chat")

        messages.append({
            "role": "user",
            "content": user_input
        })

    ai_reply = ask_llm(messages)

    print(f"\nAI: {ai_reply}\n")
    messages.append({
        "role": "assistant",
        "content": ai_reply
    })