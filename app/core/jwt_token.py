import requests
from app.config.settings import UID, PASS, URL

def get_jwt():
    try:
        params = {
            'uid': UID,
            'password': PASS
        }
        response = requests.get(URL, params=params)  # GET hi sahi hai
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)

        if response.status_code == 200:
            jwt_data = response.json()
            return jwt_data.get("token")
        return None
    except Exception as e:
        print("Error:", e)
        return None

# Run
token = get_jwt()
print("JWT Token:", token)
