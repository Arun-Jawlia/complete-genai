# Read File in Different Ways

# Read all content
with open('sales_data.txt', 'r') as file:
    content = file.read()
    print('Content: ')
    print(content)

# Read First Line
with open('sales_data.txt', 'r') as file:
    content = file.readline()
    print('First Line: ')
    print(content)

# Read All lines using Readlines()
with open('sales_data.txt', 'r') as file:
    content = file.readlines()
    sales_list = []
    for line in content:
        sales_list.append(int(line))
    
    print("Read all lines and converting into list",sales_list)
        
