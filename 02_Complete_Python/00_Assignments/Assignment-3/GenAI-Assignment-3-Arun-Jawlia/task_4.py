# Using Map(): Apply Gst to List Of Prices

prices = [100, 250, 400, 1200, 50]

new_price_list_with_gst = list(map(lambda price: price + (price*18)/ 100, prices))

print("Original Price: ", prices)
print( "Price with GST :",new_price_list_with_gst)