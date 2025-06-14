from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MoodWeatherMapViewSet, MoodWeatherView

router = DefaultRouter()
router.register(r'mood-mapping', MoodWeatherMapViewSet)

urlpatterns = [
    path('check/', MoodWeatherView.as_view()),
    path('', include(router.urls)),
]