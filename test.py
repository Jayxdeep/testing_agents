from ollama import chat
import requests

messages = []


def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": 12.97,  # Bengaluru
        "longitude": 77.59,
        "current": "temperature_2m,relative_humidity_2m"
    }

    response = requests.get(url, params=params)
    data = response.json()

    temp = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]

    return f"Temperature: {temp}°C, Humidity: {humidity}%"


print("Local AI Chat Started! Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Ending chat...")
        break

    # WEATHER + NORMAL CHAT TOGETHER
    if "weather" in user_input.lower():

       # print("\nFetching weather data...\n")

        weather_info = get_weather()

        enhanced_prompt = f"""
User Question:
{user_input}

Real-time Weather Data:
{weather_info}

Instructions:
- Answer the user's complete question.
- Use the weather data if relevant.
- If the user asked multiple things, answer all of them.
"""

        messages.append(
            {
                "role": "user",
                "content": enhanced_prompt
            }
        )

        response = chat(
            model="qwen2.5:7b",
            messages=messages
        )

        ai_reply = response["message"]["content"]

        print(f"\nAI: {ai_reply}\n")

        messages.append(
            {
                "role": "assistant",
                "content": ai_reply
            }
        )

        continue

    # NORMAL CONVERSATION
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    response = chat(
        model="qwen2.5:7b",
        messages=messages
    )

    ai_reply = response["message"]["content"]

    print(f"\nAI: {ai_reply}\n")

    messages.append(
        {
            "role": "assistant",
            "content": ai_reply
        }
    )