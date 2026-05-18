
# Loop Control with Conditions ( break & continue )

daily_sales = [200, 150, 0, 400, 50, -1, 300]

while True:
    total_sales = 0
    for sale in daily_sales:
        if sale < 0:
            print("Corrupted data")
            break
        elif sale == 0 :
            print("No Sales today")
            continue
        else:
            total_sales += sale

        print("Total Running Sale: ", total_sales)
    
    print('Total Sales', total_sales)
    break

