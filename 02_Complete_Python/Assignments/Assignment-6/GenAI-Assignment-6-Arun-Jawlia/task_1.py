# Safe Divison Utility


try:
    numerator = int(input("Enter the numerator value: "))
    denominator = int(input("Enter the denominator value: "))
    result = numerator / denominator

except ZeroDivisionError as zde:
    print("Zero Divison Error",zde)
except ValueError as ve:
    print(ve)
else:
    print("Result", result)
finally:
    print("Operation Completed")