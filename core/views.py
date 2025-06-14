# core/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from .utils import get_weather, get_song_recommendation, does_mood_match_weather
from rest_framework import viewsets
from .serializers import MoodWeatherMapSerializer
from .models import MoodWeatherMap
from rest_framework import status

class MoodWeatherView(APIView):
    def post(self, request):
        mood = request.data.get("mood")
        city = request.data.get("city")

        if not mood or not city:
            return Response({"error": "Both 'mood' and 'city' are required fields."},status=status.HTTP_400_BAD_REQUEST)
        try:
            weather_data = get_weather(city)
        except ValueError as e:
            return Response({"error": str(e)},status=status.HTTP_400_BAD_REQUEST)

        weather_desc = weather_data["weather"][0]["description"]
        mood_match = does_mood_match_weather(mood, weather_desc)

        try:
            song_data = get_song_recommendation(mood)
            tracks = song_data.get("tracks", {}).get("track", [])
            recommended_song = tracks[0].get("name") if tracks else "No song found"
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

        return Response({
            "mood": mood,
            "city": city,
            "weather": weather_desc,
            "mood_matches_weather": mood_match,
            "recommended_song": recommended_song
        })


class MoodWeatherMapViewSet(viewsets.ModelViewSet):
    queryset = MoodWeatherMap.objects.all()
    serializer_class = MoodWeatherMapSerializer