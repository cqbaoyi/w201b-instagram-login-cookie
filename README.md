# Instagram Login Cookie

Lightweight Python tool for Instagram login using direct HTTP requests. Extracts and validates authentication cookies without browser automation.

## Features

- Direct HTTP requests to Instagram login endpoints
- Automatic cookie extraction and validation
- No browser automation (Selenium, Playwright, etc.)
- Secure credential handling via user input
- JSON cookie output for reuse

## Usage

1. Install dependencies: `pip install -r requirements.txt`
2. Run: `python main.py`
3. Enter your Instagram credentials when prompted
4. Response data and cookies are saved to `data/response.json`
5. Console displays login status, validation results, and extracted data