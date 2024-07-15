import requests
import requests_cache

url = "https://api.open-meteo.com/v1/forecast"
default_current = ["temperature_2m", "relative_humidity_2m",
                   "apparent_temperature", "is_day", "precipitation",
                   "weather_code", "surface_pressure", "wind_speed_10m"]

default_hourly = ["temperature_2m", "uv_index"]

default_daily = ["temperature_2m_max", "temperature_2m_min",
                 "sunrise", "sunset", "uv_index_max"]

def get_api_response(latitude, longitude, timezone="auto", **kwargs):
    session = requests_cache.CachedSession('weather_cache', expire_after=900)

    params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": default_current,
            "hourly": default_hourly,
            "daily": default_daily,
            "timezone": timezone,
    }
    response = session.get(url, params=params)

    return response

def get_current_weather(response):
    return response.json()["current"]

def get_units(response, which="current"):
    unit_string = "{}_units".format(which)
    return response.json()[unit_string]

def get_daily_weather(response):
    return response.json()["daily"]

def get_today_weather(response):
    daily = get_daily_weather(response)

    return {
        "time": daily["time"][0],
        "temperature_2m_max": daily["temperature_2m_max"][0],
        "temperature_2m_min": daily["temperature_2m_min"][0],
        "sunrise": daily["sunrise"][0],
        "sunset": daily["sunset"][0],
        "uv_index_max": daily["uv_index_max"][0],
        }
        
def get_forecast_temperature(response):
    return response.json()["hourly"]["temperature_2m"]

def get_weather_code(response):
    return response.json()["current"]["weather_code"]

def get_time_of_day(response):
    return response.json()["current"]["is_day"]

def get_string_time_of_day(response):
    if (get_time_of_day(response)):
        return "day"
    else:
        return "night"

def get_hourly_data(response):
    return response.json()["hourly"]

if __name__ == "__main__":
    default_timezone = "Asia/Kolkata"
    params = {
            "latitude": 13.0878,
            "longitude": 80.2785,
            "current": default_current,
            "hourly": default_hourly,
            "daily": default_daily,
            "timezone": default_timezone,
    }
    response = get_api_response(**params)

    print(response.json())
    
    units = response.json()["current_units"]
    current = response.json()["current"]

    print(get_today_weather(response))

    print(get_units(response, "hourly"))

"""    
    print("The current weather in chennai:")

    for key, value in current.items():
        print(key, ": ", value, units[key])
"""
