# Append New Sales

new_sales = [5000, 2500, 1700]

with open("sales_data.txt", 'a') as file:
    for amt in new_sales:
        file.write(str(amt) + '\n')

# Reopen the file 
with open("sales_data.txt", "r") as file:

    content = file.read()

    print("New Sales Content \n: ")
    print(content)

# No of Lines
with open("sales_data.txt", "r") as file:

    content = file.readlines()

    print("No of lines: ", len(content))