import requests
import requests
import webbrowser
from urllib.parse import urlencode



api_key = '98ikekm9n8s57wtq1nancxfz'
shop_id = '577729910'
listing_id = None

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {api_key}
}

base_url = 'https://api.etsy.com/v3/'

def create_digital_listing():
    url = f'{base_url}application/shops/{shop_id}/listings'
    listing_data = {
        'title': 'Sample Digital Listing',
        'description': 'This is a sample digital listing.',
        'price': '25.00',
        'quantity': 1,
        'who_made': 'i_did',
        'is_supply': False,
        'when_made': 'made_to_order',
        'is_digital': True
    }

    response = requests.post(url, json=listing_data, headers=headers)

    if response.status_code == 201:
        listing_id = response.json()['results'][0]['listing_id']
        print(f'Listing created with ID: {listing_id}')
        return listing_id
    else:
        print(f'Failed to create listing. Status code: {response.status_code}, response text: {response.text}')
        return None

def upload_digital_file(listing_id, file_path):
    url = f'{base_url}application/listings/{listing_id}/files'

    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files, headers=headers)

    if response.status_code == 201:
        print(f'Successfully uploaded file: {file_path}')
    else:
        print(f'Failed to upload file: {file_path}. Status code: {response.status_code}, response text: {response.text}')

listing_id = create_digital_listing()
if listing_id:
    file_path = r"C:\Users\Rau\Documents\ShareX\Screenshots\2023-04\ES_nTqBrrhtrq.png"
    upload_digital_file(listing_id, file_path)

