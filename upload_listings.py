import requests
from requests_oauthlib import OAuth1

API_KEY = "cpw4vr97ap6h7po3wnlze8kt"
API_SECRET = "lyk2jqo685"
ACCESS_TOKEN = "your_access_token"
ACCESS_TOKEN_SECRET = "your_access_token_secret"

# Set up OAuth1 authentication
auth = OAuth1(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

# Define listing data
listing_data = {
    "quantity": 1,
    "title": "Sample Product",
    "description": "This is a sample product listing.",
    "price": 19.99,
    "taxonomy_id": 688,  # You can find taxonomy IDs in Etsy's taxonomy API: https://developers.etsy.com/documentation/reference#operation/getAllTaxonomy
    "who_made": "i_did",
    "is_supply": "false",
    "when_made": "made_to_order",
}

# Make the API request
response = requests.post(
    "https://openapi.etsy.com/v3/application/listings", data=listing_data, auth=auth
)

# Check if the request was successful
if response.status_code == 201:
    print("Listing created successfully!")
    print(response.json())
else:
    print("Error creating listing:", response.text)
