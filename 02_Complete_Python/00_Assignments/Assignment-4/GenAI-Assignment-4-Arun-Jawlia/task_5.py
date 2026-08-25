

with open("products.txt", 'w') as file:

    for i in range(3):

        product_name = input("Enter the product name: ")
        product_price = input("Enter the product price: ")

        file.write(f"{product_name} | {product_price} \n")

# Read and print file contents
with open("products.txt", "r") as file:

    lines = file.readlines()

    for line in lines:

        line = line.strip()
        data = line.split("|")

        product = data[0].strip()
        price = data[1].strip()

        print(f"Product Name: {product} and Its Price: Rs. {price}")