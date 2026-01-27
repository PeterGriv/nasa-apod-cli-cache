import requests
import json
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok = True)

# CREATE .IMG 
def save_image(data):
    title = data["title"]
    place_img = f"{OUTPUT_DIR}/{title}.jpg"
    img_url = data["hdurl"]
    img_data = requests.get(img_url, timeout=10).content
    with open(place_img, "wb") as f:
        f.write(img_data)


# CREATE .TXT
def save_meta(data):
    title = data["title"]
    place_txt = f"{OUTPUT_DIR}/{title}.txt"
    with open(place_txt, "w") as f:
        json.dump(data, f, indent=2)