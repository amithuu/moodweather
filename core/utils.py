import os
import requests
from .models import MoodWeatherMap


def get_weather(city: str) -> dict:
    url = (f"http://api.openweathermap.org/data/2.5/weather"f"?q={city}&appid={os.getenv('OPENWEATHER_API_KEY')}&units=metric")
    response = requests.get(url)

    try:
        data = response.json()
    except ValueError:
        # Non-JSON response
        raise ValueError("Invalid response from weather service.")

    if response.status_code == 200:
        return data
    else:
        # OpenWeatherMap returns {"cod": "...", "message": "..."}
        message = data.get("message", "Unknown error from weather service.")
        raise ValueError(message)


def get_song_recommendation(mood:str)-> dict:
    url = f"http://ws.audioscrobbler.com/2.0/?method=tag.gettoptracks&tag={mood}&api_key={os.getenv('LASTFM_API_KEY')}&format=json"
    response = requests.get(url)

    try:
        data = response.json()
    except ValueError:
        raise ValueError("Invalid response from song service.")

    if response.status_code == 200:
        # Sometimes Last.fm returns status 200 but missing expected data
        if "tracks" not in data or "track" not in data["tracks"]:
            raise ValueError("No song data found for mood: " + mood)
        return data
    else:
        message = data.get("message", "Unknown error from song service.")
        raise ValueError(message)
    

def does_mood_match_weather(mood, weather_desc):
    try:
        mapping = MoodWeatherMap.objects.get(mood_type__iexact=mood)
        return any(keyword.lower() in weather_desc.lower() for keyword in mapping.weather_keywords)
    except MoodWeatherMap.DoesNotExist:
        return False 

# def does_mood_match_weather(mood, weather_desc):
#     mood_weather_map = {
#         "happy": ["clear", "sunny"],
#         "sad": ["rain", "drizzle"],
#         "angry": ["storm", "thunder"],
#         "calm": ["clouds", "mist"],
#     }
    
#     return (w in weather_desc.lower() for w in mood_weather_map.get(mood.lower(), []))
#     # Check if any of the weather descriptions match the mood
#     # Return True if any match, otherwise False