# main.py

import json
from api_client import fetch_products
from validatorsfull import validate_products

def main():
    print("🔍 Fetching product data from API...")
    products = fetch_products()

    if not products:
        print("❌ No products retrieved or failed to fetch data.")
        return

    print(f"✅ Retrieved {len(products)} products. Starting validation...\n")

    valid_products, _ = validate_products(products)

    print(f"✅ Found {len(valid_products)} valid products:\n")

    for product in valid_products:
        print(json.dumps(product, indent=2))
        print("-" * 60)

if __name__ == "__main__":
    main()
