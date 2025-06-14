from rest_framework import serializers
from .models import MoodWeatherMap

class MoodWeatherMapSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoodWeatherMap
        fields = '__all__'
