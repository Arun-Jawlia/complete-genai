#  Generate Summary Report from File

with open('sales_data.txt', "r")as file:
    lines = file.readlines()

    sales = []
    total_sales = 0
    
    for amt in lines:
        sales.append(int(amt))
    
    max_sale = sales[0]
    min_sale = sales[0]
    average_sale = 0

    for sale in sales:
        total_sales+= sale


        if sale > max_sale:
            max_sale = sale

        if sale < min_sale:
            min_sale = sale
    
    average_sale = total_sales / len(sales)
        


    print("Total Sales: ", total_sales)
    print("Max Sale : ", max_sale)
    print("Min Sale: ", min_sale)
    print(f"Average Sale: {average_sale:.2f}")
        


    