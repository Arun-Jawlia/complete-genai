# PolyMorphism
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_info(self):
        print(f"Product: {self.name}")
        print(f"Price: ₹{self.price}")


class LaptopProduct(Product):
    def __init__(self, name, price, ram, processor):
        super().__init__(name, price)
        self.ram = ram
        self.processor = processor

    def get_info(self):
        print(f"Laptop Name : {self.name}")
        print(f"Price : ₹{self.price}")
        print(f"RAM : {self.ram}")
        print(f"Processo : {self.processor}")


class MobileProduct(Product):
    def __init__(self, name, price, camera, battery):
        super().__init__(name, price)
        self.camera = camera
        self.battery = battery

    def get_info(self):
        print(f"Mobile Name : {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Camera: {self.camera}")
        print(f"Battery: {self.battery}")

laptop1 = LaptopProduct("MacBook", 150000,"40 GB","M3")
laptop2 = LaptopProduct("Lenovo",120000," 64 GB","Intel")

mobile1 = MobileProduct("iPhone",80000, "48mp","4500")
mobile2 = MobileProduct("Samsung",70000, "12mp","5000")


products = [laptop1, mobile1, laptop2, mobile2]
for product in products:
    product.get_info()
