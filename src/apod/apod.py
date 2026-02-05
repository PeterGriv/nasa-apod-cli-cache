import sys
import requests
from dotenv import load_dotenv
from formatter import apod_to_markdown

from api import get_apod_data
from storage import save_image, save_meta, save_markdown

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
        if date != None:
            print(f"Now I am trying to fetch data for image and metadata from {date}...")
        else:
            print(f"Now I am trying to fetch data for image and metadata from today...")
        save_image(data)
        # save_meta(data)
        
        md = apod_to_markdown(data)
        save_markdown(md, data["title"])
    except requests.RequestException as e:
        print(f"Network error: {e}")
    except KeyError as e: 
        print(f"Key Error: {e}")
    except Exception as e:
        print(f"Problem: {e}")


if __name__ == "__main__":
    main()