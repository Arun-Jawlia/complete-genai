# Constructor and Encapsulation

class Product:
    def __init__(self, name, category, price):
        self.name = name
        self.category = category 
        self.price = price

    def get_info(self):
        print(f"Product is {self.name} and Price is {self.price} and Category is {self.category}")


# I Child Class
class ElectronicProduct(Product):
    def __init__(self, name, category, price, warranty_years):
        super().__init__(name, price,category )
        self.warranty_years = warranty_years

    # Method Overriding 
    def get_info(self):
        print(f"Product is {self.name} and Price is {self.price} and Category is {self.category}, Warranty is {self.warranty_years}")
        



p1 = ElectronicProduct("Laptop", "Electronics", 60000, "1 Years")
p2 = ElectronicProduct("Webcam", "Camera", 5999, '2 Years')

p1.get_info()
p2.get_info()
