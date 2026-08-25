import Math_utils
from Math_utils import square
import string_utils
import shop_package.discount as disc
from shop_package.billing import calculate_total


# Math utils functions 
print("ADD:", Math_utils.add(10,20))

print("SUBSTRACT: ",Math_utils.substract(1000, 250))

print("Square: ", square(25))

print(
    '\n'
)

# String Utils functions

str1 = 'Hi, I am arun and I am learning GenAI'

print(string_utils.capitalize_word(str1))
print(string_utils.reverse_string(str1))
print(string_utils.word_count(str1))

print(
    '\n'
)
# Discount and Billing Functions

print("Apply Discount: ", disc.apply_discount(1000, 10))

print("Total Bill: ", calculate_total([100,200,300]))