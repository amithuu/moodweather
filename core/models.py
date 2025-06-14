from django.db import models

class MoodQuery(models.Model):
    mood = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    matched = models.BooleanField()
    song = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    
class MoodWeatherMap(models.Model):
    mood_type = models.CharField(max_length=50, unique=True)
    weather_keywords = models.JSONField(help_text="List of weather keywords like ['clear', 'sunny']")
    
    def __str__(self):
        return self.mood_type