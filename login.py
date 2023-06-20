import requests
import envs
import paths

url = paths.bo_auth_url
login = envs.bo_login
password = envs.bo_password

def get_authenticated_session():
    """Logs into the website and returns the authenticated session."""
    login_data = {
        "login": login,
        "password": password,
    }

    # Start a session and log in to the website
    session = requests.Session()
    response = session.post(url, data=login_data)

    # Check if login was successful
    if response.status_code == 200:
        print("Logged in successfully")
        return session
    else:
        print("Error logging in")
        session.close()
        return None