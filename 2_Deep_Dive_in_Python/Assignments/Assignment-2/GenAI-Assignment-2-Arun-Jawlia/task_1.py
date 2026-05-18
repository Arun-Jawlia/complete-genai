"""
# Discount Rules ( if / elif / else)
"""

order_input = input("Enter the order amount: ")

if order_input.replace('.', '', 1).isdigit():
    order_amount = float(order_input)
    if order_amount >= 2000:
        discount = 15
    elif order_amount >= 1500 and order_amount< 2000:
        discount = 10
    elif order_amount >= 1000 and order_amount< 1500:
        discount = 7
    else:
        discount = 0

    calulate_discount = ( order_amount * discount ) / 100
    sub_total = order_amount - calulate_discount 

    tax = ( sub_total * 5 ) / 100

    final_amount = sub_total + tax

    print(f'Final Amount after {discount} % discount and 5 % tax is {final_amount}')
else:
    print('Enter the Positive Value')