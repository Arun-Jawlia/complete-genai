
#  Recursive Function: Factorial Utility

def factorial(n):
    if n < 0:
        return "Error: N is negative"

    if n == 0 or n == 1:
        return 1
    fact = n * factorial(n - 1)
    return fact

print(factorial(5))
print(factorial(0))
print(factorial(-3))


