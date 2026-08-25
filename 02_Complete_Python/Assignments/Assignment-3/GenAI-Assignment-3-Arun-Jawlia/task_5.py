# Using Filter(): Filter Expensive Products

prices = [100,250, 400, 1200, 50, 2000, 850]

prices_greater_than_500 = list(filter(lambda price: price > 500, prices))
prices_less_than_500 = list(filter(lambda price: price <= 500, prices))

print("original price lists: ", prices)
print("Price lists greater than 500: ", prices_greater_than_500)
print("Price lists less than 500 or equal to 500: ", prices_less_than_500)