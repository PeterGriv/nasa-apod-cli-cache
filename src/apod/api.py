import requests
import os 

def get_apod_data():
    NASA_API_KEY = os.getenv("NASA_API_KEY")
    if not NASA_API_KEY:
        raise RuntimeError("API KEY not set!")
    source = requests.get(
        "https://api.nasa.gov/planetary/apod", 
        params={"api_key" : NASA_API_KEY}, timeout=10)
    source.raise_for_status()
    data = source.json()
    return data