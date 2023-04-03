import requests

api_key = '98ikekm9n8s57wtq1nancxfz'
shop_id = '33368777'
listing_id = None

# Step 1: Create a new listing
listing_url = f'https://api.etsy.com/v3/application/shops/{shop_id}/listings'

listing_data = {
    'title': 'Sample Listing',
    'description': 'This is a sample listing.',
    'price': '25.00',
    'quantity': 1,
    'who_made': 'i_did',
    'is_supply': False,
    'when_made': 'made_to_order',
}

headers = {
    'Content-Type': 'application/json',
    'x-api-key': api_key,
}

response = requests.post(listing_url, json=listing_data, headers=headers)

if response.status_code == 201:
    listing = response.json()
    listing_id = listing['results'][0]['listing_id']
    print(f'Listing created with ID: {listing_id}')
else:
    print(f'Failed to create listing. Status code: {response.status_code}')

# Step 2: Upload images to the listing
if listing_id is not None:
    image_url = f'https://api.etsy.com/v3/application/listings/{listing_id}/images'

    # Replace with paths to your image files
    image_paths = [r"C:\Users\Rau\Documents\ShareX\Screenshots\2023-04\ES_nTqBrrhtrq.png"]

    for image_path in image_paths:
        with open(image_path, 'rb') as img_file:
            files = {'image': img_file}
            response = requests.post(image_url, headers={'x-api-key': api_key}, files=files)

            if response.status_code == 201:
                print(f'Successfully uploaded image: {image_path}')
            else:
                print(f'Failed to upload image: {image_path}. Status code: {response.status_code}')
