WEATHER_KEYWORDS=[
    "weather",
    "temperature",
    "forecast",
    "humidity",
    "rain"
]
KNOWLEGE_KEYWORDS=[
    "what",
    "why",
    "how",
    "explain",
    "define",
    "tell me"
]
def detect_intents(user_inp):
    text=user_inp.lower()
    intents=[]
    if any(keyword in text for keyword in WEATHER_KEYWORDS):
        intents.append("weather")
    if any(keyword in text for keyword in KNOWLEGE_KEYWORDS):
        intents.append("knowledge")
    return intents