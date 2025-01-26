import requests


def get_weather_data(city):
    """
    Fetches weather data for a given city using an external API.
    """
    api_key = "your_api_key"
    base_url = f"http://api.weather.com/v1/current?city={city}&key={api_key}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data.get("temperature"), data.get("condition")
    else:
        raise ValueError("Failed to fetch weather data")