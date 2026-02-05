import requests
import json
import os

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok = True)

# SAVE .IMG 
def save_image(data):
    title = data["title"]
    place_img = f"{OUTPUT_DIR}/{title}.jpg"
    img_url = data["hdurl"]
    img_data = requests.get(img_url, timeout=10).content
    with open(place_img, "wb") as f:
        f.write(img_data)


# # SAVE METADATA
# def save_meta(data):
#     title = data["title"]
#     place_txt = f"{OUTPUT_DIR}/{title}.txt"
#     with open(place_txt, "w") as f:
#         json.dump(data, f, indent=2)


# CREATE MARKDOWN
def save_markdown(markdown_text: str, title: str):
    place_md = f"{OUTPUT_DIR}/{title}.md"
    with open(place_md, "w", encoding="utf-8") as f:
        f.write(markdown_text)


# SAVE HTML 
def save_html(html_text: str, title: str) -> str:
    place_html = f"{OUTPUT_DIR}/{title}.html"
    with open(place_html, "w", encoding="utf-8") as f:
        f.write(html_text)
    return place_html