
#  Write Sales Records a File

sales = [1200, 450, 980, 1500, 3000]

with open("sales_data.txt", 'w') as file:
    for amount in sales:
        file.write(str(amount) + "\n")

with open('sales_data.txt', "r") as file:
    file_content = file.read()
    print(file_content)

