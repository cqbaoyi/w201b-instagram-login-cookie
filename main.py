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
        with open("data/response.json", 'w') as f:
            json.dump(response_data, f, indent=2)
            json.dump(cookies, f, indent=2)
        print(f"Login successful! Cookies saved to data/response.json")
        print(f"Extracted {len(cookies)} fields in the cookies")
        
        # Validate cookies
        if login_handler.validate_cookies(cookies):
            print("✅ Cookie validation successful - authentication confirmed!")
            print(response_data)
            print(cookies)
        else:
            print("❌ Cookie validation failed - cookies may not be valid")
    else:
        print("Login failed. Please check your credentials.")


if __name__ == "__main__":
    main()
