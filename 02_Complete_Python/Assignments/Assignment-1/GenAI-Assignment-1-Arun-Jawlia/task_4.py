
# COMBINED OPERATIONS

products = ["laptop","tablet","smartphone","headphones","smartwatch","camera"]

# Prices dictionary
price_dict = { "laptop": 99999, "tablet": 49999, "smartphone": 69999, "headphones": 14999, "smartwatch": 24999, "camera": 79999 }

categories_dict = {
    "laptop": "electronics",
    "tablet": "electronics",
    "smartphone": "electronics",
    "headphones": "accessories",
    "smartwatch": "wearable",
    "camera": "electronics"
}

catalog = []

for item in products:
    price = price_dict[item]
    category = categories_dict[item]

    catalog.append((item, price, category))

print('\n')
print("Catalog: ", catalog)

# Create categories_to_products dictionary
categories_to_products = {}

for product, price, category in catalog:

    if category not in categories_to_products:
        categories_to_products[category] = []

    categories_to_products[category].append(product)

# Categories
print('\n')
print("Categories to Products:" ,categories_to_products)

# Find category with maximum number of products
max_category = max(
    categories_to_products,
    key=lambda category: len(categories_to_products[category])
)

print('\n')
# Print products in that category
print(f"Category with maximum products: {max_category}")

for product in categories_to_products[max_category]:
    print(product)
