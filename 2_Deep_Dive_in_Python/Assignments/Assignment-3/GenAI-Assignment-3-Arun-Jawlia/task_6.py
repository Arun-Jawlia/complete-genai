
#  Combined Utitiy Function

def process_prices(prices):
    discount_prices = list(map(lambda price: price - (price*10)/100, prices))
    filtered_prices = list(filter(lambda price: price> 300, discount_prices))

    return discount_prices, filtered_prices

discount_prices, filtered_prices =  process_prices([100, 500, 900, 50, 750])
print(discount_prices)
print(filtered_prices)