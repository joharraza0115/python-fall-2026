# sample_weather.py

def get_todays_weather():
    weather = {
        "location": "Sterling, VA",
        "current_temp": "68°F",
        "high": "78°F",
        "low": "68°F",
        "conditions": "Mostly cloudy",
        "wind": "NNE 5 mph",
        "air_quality": "Fair"
    }
    return weather

if __name__ == "__main__":
    w = get_todays_weather()
    print(f"Today's Weather for {w['location']}")
    print(f"Current Temperature: {w['current_temp']}")
    print(f"High: {w['high']} | Low: {w['low']}")
    print(f"Conditions: {w['conditions']}")
    print(f"Wind: {w['wind']}")
    print(f"Air Quality: {w['air_quality']}")
