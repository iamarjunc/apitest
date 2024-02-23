import requests

# URL for the books endpoint
url = "http://127.0.0.1:8000/authors/"

# Obtain JWT tokens using credentials (username and password)
def obtain_tokens():
    login_url = "http://127.0.0.1:8000/api/token/"
    credentials = {
        "username": "Admin",
        "password": "1234"
    }
    response = requests.post(login_url, data=credentials)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error obtaining tokens:", response.text)
        return None

# Get JWT tokens
tokens = obtain_tokens()
print(tokens)

if tokens:
    access_token = tokens["access"]

    # Include the token in the request headers
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"  # Optionally include content type
    }

    # Make a GET request to the books endpoint with authentication token
    response = requests.get(url, headers=headers)

    # Check the response
    if response.status_code == 200:
        # Request was successful, process the response
        print(response.json())  # or do whatever processing you need
    else:
        # Request failed, print error message
        print("Error:", response.text)
