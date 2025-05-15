# validators.py

def validate_products(products):
    defective_products = []

    for product in products:
        issues = []

        # Title check
        title = product.get("title")
        if not isinstance(title, str) or not title.strip():
            issues.append("Empty title")

        # Price check
        price = product.get("price")
        if not isinstance(price, (int, float)) or price < 0:
            issues.append("Negative or invalid price")

        # Rating.rate check
        rating = product.get("rating", {})
        rate = rating.get("rate")
        if not isinstance(rate, (int, float)) or rate > 5:
            issues.append("Rating exceeds 5 or invalid")

        if issues:
            defective_products.append({
                "id": product.get("id"),
                "title": title or "<No Title>",
                "issues": issues
            })

    return defective_products
