import requests
import json


# CREATE .IMG 
def save_image(data):
    title = data["title"]
    place_img = f"/Users/Fidel/Desktop/{title}.jpg"
    img_url = data["hdurl"]
    img_data = requests.get(img_url, timeout=10).content
    with open(place_img, "wb") as f:
        f.write(img_data)


# CREATE .TXT
def save_meta(data):
    title = data["title"]
    place_txt = f"/Users/Fidel/Desktop/{title}.txt"
    with open(place_txt, "w") as f:
        json.dump(data, f, indent=2)