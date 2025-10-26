import requests
import src.config as config


class InstagramLogin:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update(config.DEFAULT_HEADERS)
    
    def get_csrf_token(self):
        response = self.session.get(config.LOGIN_URL)
        return self.session.cookies.get('csrftoken')
    
    def login(self, username, password):
        csrf_token = self.get_csrf_token()
        if not csrf_token:
            return False, {}, {}
        
        login_data = {
            'username': username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:&:{password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        
        headers = {
            'X-CSRFToken': csrf_token,
            'X-Instagram-AJAX': '1',
            'X-Requested-With': 'XMLHttpRequest',
            'Referer': config.LOGIN_URL
        }
        
        response = self.session.post(config.LOGIN_AJAX_URL, data=login_data, headers=headers)
        
        if response.status_code == 200:
            result = response.json()
            cookies = dict(self.session.cookies)
            return result.get('authenticated', False), result, cookies
        else:
            return False, {"error": f"HTTP {response.status_code}"}, {}
    
    def validate_cookies(self, cookies):
        session = requests.Session()
        for name, value in cookies.items():
            session.cookies.set(name, value)
        
        try:
            # Test with Instagram's main page
            response = session.get('https://www.instagram.com/')
            if response.status_code == 200:
                content = response.text
                
                # Check for essential indicators of successful login
                return (
                    'sessionid' in str(session.cookies) or  # Session cookie present
                    'ds_user_id' in str(session.cookies) or  # User ID cookie present
                    'logout' in content.lower()  # Logout button present
                )
            return False
        except Exception as e:
            print(f"Validation error: {e}")
            return False
