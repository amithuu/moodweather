
# 🌤️ MoodWeather 🎵

This Django REST API takes a user's **mood** and **city**, checks if the current weather matches the mood, and returns a song recommendation based on that mood using external APIs.

---

## 🚀 Features

- Accepts **mood** and **city** as input
- Fetches real-time weather using **OpenWeatherMap API**
- Checks mood-to-weather match using a **dynamic database model**
- Recommends songs using **Last.fm API**
- Admin panel to manage mood-weather mappings
- RESTful API with full error handling
- Includes **Postman collection** and **unit tests**

---

## 🧰 Tech Stack

- Python 3.x
- Django 4.x
- Django REST Framework
- OpenWeatherMap API
- Last.fm API
- JSONField (for dynamic mapping)
- dotenv (for secure API keys)
- Postman (for API testing)

---

## 📦 Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/amithuu/moodweather
cd moodweather

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add API keys to .env
touch .env
```

Example `.env` file:
```
OPENWEATHER_API_KEY=your_openweathermap_api_key
LASTFM_API_KEY=your_lastfm_api_key
```

```bash
# 5. Run migrations and start server
python manage.py migrate
python manage.py runserver
```

---

## 🧪 Testing

```bash
python manage.py test
```

---

## 📫 API Endpoints

### `POST /api/check/`

```json
{
  "mood": "happy",
  "city": "Bangalore"
}
```

Response:

```json
{
  "mood": "happy",
  "city": "Bangalore",
  "weather": "clear sky",
  "mood_matches_weather": true,
  "recommended_song": "Happy by Pharrell Williams"
}
```

---

### `GET/POST /api/mood-mapping/`

CRUD for mood-to-weather keyword mapping.

---

## 🧠 Architecture

1. User submits mood + city
2. Weather is fetched from OpenWeatherMap
3. Weather description is matched with mood keywords (from DB)
4. Song recommendation is fetched from Last.fm
5. API returns mood, weather, match result, and song

---

## 🔒 Security

- Secrets stored in `.env` (not committed)
- API rate limits and error handling built-in

---

## 🧑‍💻 Author

**Amith Kulkarni**  
Python Developer | Bangalore  
GitHub: [@amithuu](https://github.com/amithuu)

---

## 📄 License

MIT License
