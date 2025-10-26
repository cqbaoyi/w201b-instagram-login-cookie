import json
import os
from src.login import InstagramLogin


def main():
    username = input("Enter Instagram username: ")
    password = input("Enter Instagram password: ")
    
    if not username or not password:
        print("Username and password are required.")
        return
    
    login_handler = InstagramLogin()
    success, response_data, cookies = login_handler.login(username, password)
    
    if success:
        os.makedirs("data", exist_ok=True)
        with open("data/cookies.json", 'w') as f:
            json.dump(cookies, f, indent=2)
        print(f"Login successful! Cookies saved to data/cookies.json")
        print(f"Extracted {len(cookies)} cookies")
    else:
        print("Login failed. Please check your credentials.")


if __name__ == "__main__":
    main()
