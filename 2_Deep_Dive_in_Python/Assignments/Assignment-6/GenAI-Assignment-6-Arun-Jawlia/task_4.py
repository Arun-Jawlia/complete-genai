# File Reader with Exception Handling:

try:
    file_name = input("Enter your file name: ")

    with open(file_name, 'r' ) as file:

        for line in range(3):
            content = file.readline()
            if content == "":
                break
            print(content.strip())
            
except FileNotFoundError as error:
    print("Error", error)
except PermissionError as error:
    print("Permission Error: ", error)
finally:
    print("File Operation attempted")