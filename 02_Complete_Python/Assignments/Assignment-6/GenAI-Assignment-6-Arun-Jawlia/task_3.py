# Task 3: Custome Exception : Age Validator

def check_age():
    try:
        age = int(input("Enter age: "))
        if age < 0 or age > 120:
            raise ValueError("Age must be between 0 and 120.")

        print("Valid Age:", age)

    except ValueError as error:
        print("Error:", error)

check_age()