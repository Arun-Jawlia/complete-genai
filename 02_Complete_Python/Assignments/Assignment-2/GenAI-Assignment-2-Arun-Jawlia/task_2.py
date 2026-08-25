# Process Multiple Orders ( for loop )

orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
discount_orders = 0

for order_amt in orders:

    if order_amt >= 2000:
        discount = 15
    elif order_amt >= 1500 and order_amt< 2000:
        discount = 10
    elif order_amt >= 1000 and order_amt< 1500:
        discount = 7
    else:
        
        discount = 0

    calulate_discount = ( order_amt * discount ) / 100

    final_amount = order_amt - calulate_discount
    total_revenue  += final_amount

    if discount > 0:
        discount_orders += 1

    print(f"Order Amount: {order_amt} | clear discount: { discount } % | final amount:  {final_amount}")

print("Total Revenue: ", total_revenue)
print("Orders with Discount: ", discount_orders)