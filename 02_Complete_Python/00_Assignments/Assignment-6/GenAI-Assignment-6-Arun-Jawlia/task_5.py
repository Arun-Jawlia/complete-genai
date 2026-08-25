# Task 5: Mini Program: Safe Shopping Cart:

cart = []

while True:

    user_input = input("Enter Price or Enter q to quit: ")

    if user_input == 'q' or user_input == 'Q':
        break

    try:
        price = float(user_input)

        if price < 0:
            raise ValueError("Pirce can't be negative")

        cart.append(price)
        print('Price addded')
    except ValueError as error:
        print(error)

total_bill = 0
for item in cart:
    total_bill+=item

print('Total Bill: ', total_bill)
print('total Items: ', len(cart))
    