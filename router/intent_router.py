def is_weather_query(user_input):
    weather_keywords=[
        "weather",
        "temperature",
        "forecast",
        "humidity",
        "rain"
    ]
    return any(
        keyword in user_input.lower()
        for keyword in weather_keywords
    )
    # return "weather" in user_input.lower()