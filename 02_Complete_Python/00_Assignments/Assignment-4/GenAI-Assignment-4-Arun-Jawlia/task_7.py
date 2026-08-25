
# Mini Project - Export Discounted Prices

prices = {
    "Mouse":500,
    "Keyboard": 800,
    "Monitor": 7000,
    "Pendrive":400,
    "Camera": 5000
}

discount = float(input("Enter your desired discount %: "))

total_discount_price = 0
total_items = len(prices)

with open("discount_report.txt", 'w') as file:

    for product in prices:

        org_price = prices[product]

        discount_price = org_price - ( org_price * discount ) / 100

        total_discount_price += discount_price

        file.write(f"{product} | {str(org_price)} | {str(discount_price)} \n")

    avg_dicount_price = total_discount_price / total_items
    file.write("Total Items: " + str(total_items) + "\n")
    file.write('Average discount Price: '+ str(avg_dicount_price) + '\n')

with open('discount_report.txt', 'r') as file:
    content = file.read()

    print("Content: ")
    print(content)