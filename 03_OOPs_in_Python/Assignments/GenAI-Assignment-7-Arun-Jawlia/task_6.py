
# Magic Methods & Operator Overloading

class Product:
    def __init__(self, name ,category, price):
        self.name = name
        self.price = price
        self.category = category

    def __str__(self):
        return f"""
        Product Name: {self.name}
        Product Price: {self.price}
        Product Category: {self.category}
        """

    def __add__(self, other):
        return self.price + other.price

p1 = Product("Laptop", "Electronices", 125637)
p2 = Product("WebCam", "Cameras", 2600)

print(p1)
print(p2)

total_price = p1 + p2

print("Total Price is : ", total_price)