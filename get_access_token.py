import requests
import webbrowser
from urllib.parse import urlencode
import secrets


state = secrets.token_hex(16)
client_id = '98ikekm9n8s57wtq1nancxfz'
client_secret = 'g43vmoqndj'
redirect_uri = 'http://localhost:8000/callback'
scope = 'listings_r listings_w listings_digital_r listings_digital_w'

# Step 1: Generate the authorization URL
auth_url = 'https://www.etsy.com/oauth/connect'
params = {
    'client_id': client_id,
    'response_type': 'code',
    'scope': scope,
    'redirect_uri': redirect_uri
}
authorization_url = f"{auth_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&state={state}"


# Step 2: Redirect the user to the authorization URL
print(f"Please visit the following URL in your browser and authorize the application: {authorization_url}")
webbrowser.open(authorization_url)

# Step 3: Obtain the authorization code from the user
authorization_code = input("Enter the authorization code provided by Etsy: ")

# Step 4: Exchange the authorization code for an access token
token_url = 'https://api.etsy.com/v3/public/oauth/token'
token_data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'code': authorization_code,
    'grant_type': 'authorization_code',
    'redirect_uri': redirect_uri
}
response = requests.post(token_url, data=token_data)

if response.status_code == 200:
    access_token = response.json()['access_token']
    print(f"Access token: {access_token}")
else:
    print(f"Failed to obtain access token. Status code: {response.status_code}, response text: {response.text}")
