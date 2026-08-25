# TASK 2: Bill calculator with Error handling

prices = [120, 350, 'abc', 500, -200, 800]

total = 0

for price in prices:
    try:
        if not isinstance(price, (int,float)):
            raise TypeError("Invalid Type Found")
        
        if price < 0:
            raise ValueError("Negative Price not allowed")
        
        total += price

        print('Running Total', total)
    except TypeError as error:
        print("Type error", error)

    except ValueError as error:
        print("Value Error:", error)

print("Final Total: ", total)

