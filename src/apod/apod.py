import requests, json
import os 
from dotenv import load_dotenv
load_dotenv()

# GET DATA from API 
NASA_API_KEY = os.getenv("NASA_API_KEY")
source = requests.get("https://api.nasa.gov/planetary/apod", params={"api_key" : NASA_API_KEY}, timeout=10)
data = source.json()
print(data)

# CREATE IMG 
title = data["title"]
place_img = f"/Users/Fidel/Desktop/{title}.jpg"
img_url = data["hdurl"]
img_data = requests.get(img_url, timeout=10).content
with open(place_img, "wb") as f:
    f.write(img_data)


# CREATE TXT
title = data["title"]
place_txt = f"/Users/Fidel/Desktop/{title}.txt"
with open(place_txt, "w") as f:
    json.dump(data, f, indent=2)



# MAIN WRAPPER
# def main():




# if __name__ == "__main__":
#     main()