import requests
def get_weather():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 12.97,
        "longitude": 77.59,
        "current": "temperature_2m,relative_humidity_2m"
    }
    response = requests.get(url, params=params)
    data = response.json()
    temp = data["current"]["temperature_2m"]
    humidity = data["current"]["relative_humidity_2m"]
    return f"Temperature: {temp}°C, Humidity: {humidity}%"