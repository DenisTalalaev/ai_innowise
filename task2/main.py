# main.py

from api_client import fetch_products
from validators import validate_products

def main():
    print("🔍 Fetching product data from API...")
    products = fetch_products()

    if not products:
        print("❌ No products retrieved or failed to fetch data.")
        return

    print(f"✅ Retrieved {len(products)} products. Starting validation...\n")

    defects = validate_products(products)

    if defects:
        print(f"\n🚨 Found {len(defects)} defective products:\n")
        for defect in defects:
            print(f"Product ID {defect['id']} - {defect['title']}")
            for issue in defect["issues"]:
                print(f"  - {issue}")
            print("-" * 40)
    else:
        print("🎉 All products passed validation!")

if __name__ == "__main__":
    main()
