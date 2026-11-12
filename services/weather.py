import requests


def get_weather(city="Mumbai"):

    try:

        # Get coordinates
        geo_url = "https://geocoding-api.open-meteo.com/v1/search"

        geo_params = {
            "name": city,
            "count": 1,
            "language": "en",
            "format": "json"
        }

        geo_response = requests.get(
            geo_url,
            params=geo_params,
            timeout=5
        )

        geo_data = geo_response.json()

        if not geo_data.get("results"):
            return f"I couldn't find the location {city}."

        location = geo_data["results"][0]

        latitude = location["latitude"]
        longitude = location["longitude"]
        location_name = location["name"]

        # Get weather
        weather_url = "https://api.open-meteo.com/v1/forecast"

        weather_params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,apparent_temperature,weather_code",
            "timezone": "auto"
        }

        response = requests.get(
            weather_url,
            params=weather_params,
            timeout=5
        )

        data = response.json()

        current = data["current"]

        temperature = round(current["temperature_2m"])
        feels_like = round(current["apparent_temperature"])
        weather_code = current["weather_code"]

        conditions = {
            0: "clear sky",
            1: "mainly clear",
            2: "partly cloudy",
            3: "overcast",
            45: "foggy",
            48: "foggy",
            51: "light drizzle",
            53: "drizzle",
            55: "heavy drizzle",
            61: "light rain",
            63: "rain",
            65: "heavy rain",
            71: "light snow",
            73: "snow",
            75: "heavy snow",
            80: "light showers",
            81: "showers",
            82: "heavy showers",
            95: "thunderstorm"
        }

        condition = conditions.get(
            weather_code,
            "unknown conditions"
        )

        return (
            f"The weather in {location_name} is {condition}. "
            f"The temperature is {temperature} degrees Celsius, "
            f"feels like {feels_like} degrees."
        )

    except requests.RequestException:

        return "Weather service is currently unavailable."

    except Exception as e:

        print(f"Weather Error: {e}")

        return "Sorry, I couldn't fetch the weather."