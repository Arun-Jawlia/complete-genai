# User Menu ( while loop + break/continue )

orders = []

while True:

    print("Our Menu: ")
    print("Choose 1 for Add order amount: ")
    print("Choose 2 for show all orders and Total after discount: ")
    print("choose q to Quit")
    choice = input("Enter your choise: ")

    if choice == "1":
        amount = input('Enter your amount: ')
        if amount.replace('.', '', 1).isdigit():
            orders.append(float(amount))
            print("Order added successfully.")

        else:
            print("Invalid amount entered.")

        continue

    elif choice == "2":
        if len(orders) == 0:
            print("No orders found")
            continue
        
        total_revenue = 0

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
            print(f"Order Amount: {order_amt} | clear discount: { discount } % | final amount:  {final_amount}")
        
        print("Total Revenues: ", total_revenue)
        continue
    elif choice == 'q':
        print("Program ended")
        break
    else:
        print("Invalid Options")


