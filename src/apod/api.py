import requests
import os 

def get_apod_data(date=None):
    NASA_API_KEY = os.getenv("NASA_API_KEY")
    if not NASA_API_KEY:
        raise RuntimeError("API KEY not set!")
    params={"api_key" : NASA_API_KEY}
    if date:
        params["date"] = date 
    source = requests.get("https://api.nasa.gov/planetary/apod", params=params, timeout=10) 
    source.raise_for_status()
    data = source.json()
    return data