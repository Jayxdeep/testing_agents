from services.chat_service import ask_llm
from tools.weather_tool import get_weather
from memory.chat_memory import messages
from router.intent_router import is_weather_query

print("Local AI Chat Started! Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Ending chat...")
        break

    # WEATHER QUERY
    if is_weather_query(user_input):

        weather_info = get_weather()

        enhanced_prompt = f"""
User Question:
{user_input}

Weather Data:
{weather_info}

Answer the user's complete question.
Use the weather data if relevant.
If the user asks multiple things, answer all of them.
"""

        # Temporary conversation (tool context only)
        temp_messages = messages.copy()

        temp_messages.append({
            "role": "user",
            "content": enhanced_prompt
        })

        ai_reply = ask_llm(temp_messages)

        print(f"\nAI: {ai_reply}\n")

        # Store only the original conversation
        messages.append({
            "role": "user",
            "content": user_input
        })

        messages.append({
            "role": "assistant",
            "content": ai_reply
        })

        continue

    # NORMAL CHAT
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