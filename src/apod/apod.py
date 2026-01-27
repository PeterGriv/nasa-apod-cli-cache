import requests
from dotenv import load_dotenv

from api import get_apod_data
from storage import save_image, save_meta

load_dotenv()

# MAIN WRAPPER
def main():
    try: 
        data = get_apod_data()
        save_image(data)
        save_meta(data)
    except requests.RequestException as e:
        print(f"Network error: {e}")
    except KeyError as e: 
        print(f"Key Error: {e}")
    except Exception as e:
        print(f"Problem: {e}")


if __name__ == "__main__":
    main()