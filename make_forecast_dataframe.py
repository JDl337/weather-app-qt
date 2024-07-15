import pandas as pd

def make_data_frame(hourly_response):
    hourly_data = {"date": pd.date_range(
            start = pd.to_datetime(hourly_response["time"][0]),
            end = pd.to_datetime(hourly_response["time"][len(hourly_response["time"])-1]),
            freq = pd.Timedelta(seconds = 3600)
    )}
    hourly_data["temperature_2m"] = hourly_response["temperature_2m"]
    hourly_dataframe = pd.DataFrame(data = hourly_data)

    return hourly_dataframe

if __name__ == "__main__":

    import requests
    import pandas as pd
    import matplotlib.pyplot as plt
    
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
            "latitude": 13.0878,
            "longitude": 80.2785,
            "hourly": ["temperature_2m", "uv_index"],
            "timezone": "Asia/Kolkata",
    }
    response = requests.get(url, params=params)

    hourly = response.json()["hourly"]

    fig, axes = plt.subplots()
    axes.set_title("Temperature")
    axes.set_ylabel("Temperature (celcius)")

    hourly_dataframe = make_data_frame(hourly)
    hourly_dataframe.plot(ax=axes, x='date', y='temperature_2m')

    plt.show()
