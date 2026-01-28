import sys
import requests
from dotenv import load_dotenv

from api import get_apod_data
from storage import save_image, save_meta

load_dotenv()

# MAIN WRAPPER
def main():
    date = None

    if len(sys.argv) > 1:
        date = sys.argv[1]
    
    if date == "today":
        date = None


    try: 
        data = get_apod_data(date=date)
        save_image(data)
        save_meta(data)
        print("Request succesful!")
    except requests.RequestException as e:
        print(f"Network error: {e}")
    except KeyError as e: 
        print(f"Key Error: {e}")
    except Exception as e:
        print(f"Problem: {e}")


if __name__ == "__main__":
    main()