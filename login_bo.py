import requests
import envs
import paths
import pickle

url = paths.bo_auth_url
check_url = paths.bo_check_url
login = envs.bo_login
password = envs.bo_password
SESSION_FILE = "session.pkl"

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
    

def is_session_valid(session):
    response = session.get(check_url)
    return response.status_code == 200


def create_or_load_session():
    
    session = None

    try:
        with open(SESSION_FILE, "rb") as f:
            session = pickle.load(f)
            print("Loaded the existing session from file.")
            if not is_session_valid(session):
                print("Session expired. Creating a new session.")
                session = None
    except FileNotFoundError:
        pass

    if not session:
        session = get_authenticated_session()
        if session:
            with open(SESSION_FILE, "wb") as f:
                pickle.dump(session, f)
                print("Saved the new session to file.")

    return session