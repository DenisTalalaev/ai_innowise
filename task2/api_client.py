# api_client.py

import requests

API_URL = "https://fakestoreapi.com/products"

def fetch_products():
    try:
        response = requests.get(API_URL)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Unexpected status code: {response.status_code}")
            return []
    except requests.RequestException as e:
        print(f"❌ Error fetching data: {e}")
        return []
