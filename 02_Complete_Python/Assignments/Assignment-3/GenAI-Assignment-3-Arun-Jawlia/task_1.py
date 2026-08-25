
#  Task 1: Basic Function: Price After Discount

def apply_discount(price, discount = 5):
    max_discount = 60

    if discount > max_discount:
        discount = 60

    discount_amt = ( price * discount) / 100

    final_price = price - discount_amt

    return final_price

print(apply_discount(500))
print(apply_discount(2000, 40))
print(apply_discount(3000, 80))

