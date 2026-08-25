"""
Product Collections ( Lists and tuples)
"""

# Products List
products = [ "laptop", 'mouse', "monitor", "mobile", "charger", "headphone"]

print("2nd Product: ", products[1]) # index start with 0 but place 1 in list

print("Last Product: ", products[-1]) # reverse indexing

# added more than 1 product using extend func
products.extend(['macbook', "iphone"])

print("Products: ", products)

sample_product = ('Lenovo ideapad', 56000, "Electronics")

# converting into list because tuples are immutable,
sample_product_convert_into_list = list(sample_product)

print("Sample Product :", sample_product_convert_into_list)

sample_product_convert_into_list[1] = 90000

# Converting into Tuple 
sample_product_convert_into_tuple = tuple(sample_product_convert_into_list)

print("Final Sample Products :", sample_product_convert_into_tuple)