import sys
import webbrowser
from pathlib import Path

from dotenv import load_dotenv
import requests
from api import get_apod_data

from storage import save_image, save_markdown, save_html
from formatter import apod_to_markdown, apod_to_html


load_dotenv()

# MAIN WRAPPER
def main():
    date = None

    if len(sys.argv) > 1:
        date = sys.argv[1]
    if date == "today":
        date = None

    print("Welcome to the NASA APOD API CLI tool. Now I`ll try to connect to the API...")

    try: 
        data = get_apod_data(date=date)
        print("Request succesful!")
        if date is not None:
            print(f"Now I am trying to fetch data for image and metadata from {date}...")
        else:
            print(f"Now I am trying to fetch data for image and metadata from today...")
        save_image(data)
        # save_meta(data)
        
        md = apod_to_markdown(data)
        save_markdown(md, data["title"])
        html = apod_to_html(data)
        html_path = save_html(html, data["title"])
        webbrowser.open(Path(html_path).resolve().as_uri())
    except requests.RequestException as e:
        print(f"Network error: {e}")
    except KeyError as e: 
        print(f"Key Error: {e}")
    except Exception as e:
        print(f"Problem: {e}")


if __name__ == "__main__":
    main()