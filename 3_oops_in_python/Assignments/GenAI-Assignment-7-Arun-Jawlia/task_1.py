# Basic Class and Object Creation

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category 
        self.price = price

    def get_info(self):
        print(f"Product is {self.name} and Price is {self.price} and Category is {self.category}")

    def apply_discount(self, percent):

        if percent < 0 or percent > 100:
            print("Invalid Discount")


        new_price = self.price - (self.price * percent) / 100 
        print(f"Price of Product with discount {percent} % is  {new_price}")


p1 = Product("Laptop", "Electronics", 60000)
p2 = Product("Chair", "Furniture", 5999)

p1.get_info()
p1.apply_discount(10)

print("\n")

p2.get_info()
p2.apply_discount(10)


