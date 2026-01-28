# NASA APOD CLI Tool 

Simple Python CLI tool that fetches data from NASA APOD (Astronomy Picture of the Day) API, and then saves image and metadata locally. 

# What it does
- Fetches APOD data from NASA API
- Supports optional date parameter (today or specific date)
- Downloads the APOD image
- Saves metadata as JSON
- Stores output files in a local project directory

# Requirements 
Python 3.9+
NASA API Key (https://api.nasa.gov/)


# Setup 
Create and activate virtual environment: 
```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies: 
```pip install -r requirements.txt```

Create .env file in project root:
```NASA_API_KEY=your_api_key_here```


# Usage 
Run without arguments: 
```Python3 src/apod/apod.py```

Run for actual day: 
```Python3 src/apod/apod.py today``` 

Run for a specific date: 
```Python3 src/apod/apod.py 2026-01-27```


# Output 
Generated files are stored in the output/ directory: APOD image (.jpg) and metadata (.txt). 
The output/directory is created by the running program. 

# Project structure: 
src/apod/
├── apod.py      # CLI entry point
├── api.py       # API communication
├── storage.py   # Logic for file saving
