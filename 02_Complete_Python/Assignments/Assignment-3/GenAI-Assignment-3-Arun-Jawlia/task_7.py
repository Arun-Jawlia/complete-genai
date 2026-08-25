# Mini Problem: Menu Using Functions

# Add price
def add_prices(prices_list, price):
    return prices_list.append(price)

def get_average_prices(prices_list):

    if len(prices_list) == 0:
        return 0
    
    total = 0
    for price in prices_list:
        total += price

    avg = total / len(prices_list)
    return avg

# Average Price
def get_max_price(prices_list):

    if len(prices_list) == 0:
        return 0

    max_price = prices_list[0]

    for price in prices_list:
        if price > max_price:
            max_price = price

    return max_price


prices = []

while True:
    print("Our Menu: ")
    print("Choose 1 for Add Price: ")
    print("Choose 2 Show Average Price: ")
    print("Choose 3 Show Highest Price: ")
    print("choose q to Quit")
    choice = input("Enter your choise: ")   

    if choice == '1':

        value = input("Enter Prices: ")

        if value.replace(".", '', 1).isdigit():
            add_prices(prices, float(value))
            print("Price Added")
        else:
            print("Invalid Price")
        
        continue
    
    elif choice == '2':
        average = get_average_prices(prices)
        print("Average Price: ", average)
    
    elif choice == '3':
        highest_price = get_max_price(prices)
        print("Highest Price: ", highest_price)
    
    elif choice == 'q':
        print('Program ended')
        break
    else:
        print('Invalid Choise')
    


