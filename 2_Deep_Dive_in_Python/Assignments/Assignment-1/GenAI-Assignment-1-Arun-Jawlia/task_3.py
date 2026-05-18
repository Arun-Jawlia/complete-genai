"""
TASK 3: PRODUCT PRICING ( Dictionaries)
"""

price_dict = {
    "laptop": 60000,
    "tablet": 25000,
    "smartphone": 15000,
    "camera": 30000,
    "iphone 17": 150000,
    "samsung": 130000
}

def add_product(name, price):
    if name not in price_dict:
        price_dict[name] = price
        print('Product Added')
    else:
        print(f"Product with {name} is already exist")

def update_product_price(name, new_price):
    if name in price_dict:
        price_dict[name] = new_price
        print('Price Updated')
    else:
        print(f"Product: {name} is not exist")


def remove_product(name):
    if name in price_dict:
        del price_dict[name]
        print("Product Deleted")
    else:
        print(f"Product with this {name} is not found")

def average_price():
    avg_price = sum(price_dict.values()) / len(price_dict)
    print(f'Average Price:  {avg_price:.2f}')

def min_and_max_product():
    max_price = max(price_dict, key=price_dict.get)
    min_price = min(price_dict, key=price_dict.get)

    print(f'Min Price Product is :{min_price} with {price_dict[min_price]}')
    print(f'Max Price Product is :{max_price} with {price_dict[max_price]}')

add_product("printer", 10000)

print('Price_dict after adding printer: ', price_dict)

update_product_price("smartphone", 1599)

print('Price_dict after updating price of smartphone: ', price_dict)

remove_product("printer")

print('Price_dict after removing printer: ', price_dict)

average_price()

min_and_max_product()