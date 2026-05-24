
class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category
        self.price = price
    
    def __str__(self):
        return f"""
        Product: {self.name}
        Price: {self.price}
        Category: {self.category}
        """
    
    def __add__(self,other):
        return self.price + other.price

class Inventory:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)
        print("Product Added")

    def remove_product(self, product_name):
        
        for product in self.products:
            if product.name == product_name:
                self.products.remove(product)

                print("Product Deleted")
                return
        print("Product not found")
        

    def get_total_value(self):
        total = 0

        for product in self.products:
            total += product.price
        
        return total

    def show_all_products(self):
        print("All Products")
        for product in self.products:
            print(product)

class Store:
    def __init__(self, store_name):
        self.store_name = store_name
        self.inventory = Inventory()
    
    def add_new_products(self, product):
        self.inventory.add_product(product)
    
    def remove_new_products(self,product):
        self.inventory.remove_product(product)

    def show_summary(self):
        print(f"Store Name: {self.store_name}")
        self.inventory.show_all_products()

        total_items = len(self.inventory.products)

        total_value = self.inventory.get_total_value()

        print(f"Total Items: {total_items} and Total Value: {total_value}")


store_1 = Store("Arun Jawlia Store")

p1 = Product("Iphone", 'Mobiles', 156891)
p2 = Product("Laptop", 'Electronices', 236891)
p3 = Product("Sony", 'Camera', 15699)

store_1.add_new_products(p1)
store_1.add_new_products(p2)
store_1.add_new_products(p3)
store_1.show_summary()

store_1.remove_new_products(p1.name)

store_1.show_summary()

combined_price = p1 + p2
print(f"\nCombined Price of 2 Products :{combined_price}")