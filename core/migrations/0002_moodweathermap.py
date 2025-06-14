# Generated by Django 5.0.7 on 2025-06-14 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoodWeatherMap',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mood_type', models.CharField(max_length=50, unique=True)),
                ('weather_keywords', models.JSONField(help_text="List of weather keywords like ['clear', 'sunny']")),
            ],
        ),
    ]
