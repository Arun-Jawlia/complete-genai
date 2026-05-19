

# Calculate Total Price

def calculate_total(prices):
    total = 0

    for amt in prices:
        total += amt

    return total

#  apply 5 % tax
def apply_tax(amount):
    return amount + (amount*5) / 100