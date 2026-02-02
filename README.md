# nasa-apod-cli-cache 

# NASA APOD CLI Tool

Simple Python CLI tool for fetching data from NASA Astronomy Picture of the Day (APOD) API and saving the image and metadata locally.

This project is intended as a small portfolio example demonstrating:
- working with external APIs
- environment variables
- basic error handling
- modular project structure
- simple CLI argument handling

## What it does

- Fetches APOD data from the NASA API
- Supports optional date parameter (today or a specific date)
- Downloads the APOD image
- Saves metadata as a JSON file
- Stores output files in a local project directory

## Requirements

- Python 3.9+
- NASA API key  
  Get one for free at: https://api.nasa.gov/

## Setup

### 1. Create and activate virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies 
```bash
pip install requirements.txt
```

### 3. Create .env file in project root 
```bash
NASA_API_KEY=your_api_key_here
```

## Usage 
Run without arguments (fetches today’s APOD):
```bash
python src/apod/apod.py
```

Fetch APOD for a specific date:
```bash
python src/apod/apod.py 2026-01-27
```

## Output
Generated files are stored in the output/ directory:
	•	APOD image (.jpg)
	•	Metadata file (.txt / JSON format)

The output/ directory is created automatically when the program runs and is excluded from version control. 


## Project structure 
src/apod/
├── apod.py      # CLI entry point
├── api.py       # API communication logic
├── storage.py   # File saving logic


