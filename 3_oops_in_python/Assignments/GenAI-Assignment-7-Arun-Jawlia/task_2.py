# Constructor and Encapsulation

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category 
        self.__price = price

    # Getter Method
    def get_price(self):
        print(f"Price of Product is : {self.__price}")
    
    # Setter Method
    def set_price(self, new_price):
        if new_price < 0 :
            print("Invalid Price")
        
        self.__price = new_price
        print("Price Updated Successfully")


p1 = Product("Laptop", "Electronics", 60000)
p2 = Product("Chair", "Furniture", 5999)

# Price Before Change
p1.get_price()
p1.set_price(100000)
# Price After Change
p1.get_price()

print("\n")

# Price Before Change
p2.get_price()
p2.set_price(-99999)
p2.set_price(99999)
# Price After Change
p2.get_price()


