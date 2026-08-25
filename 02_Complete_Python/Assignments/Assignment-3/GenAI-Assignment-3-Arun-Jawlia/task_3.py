
#  Lambda Function: GST Calculator

# Gst with Price
gst_calculator = lambda price: price +  (price * 18) / 100

# Final price after gst and discount
final_price_after_gst = lambda price, discount : gst_calculator(price) - ( gst_calculator(price) * discount ) / 100

print(gst_calculator(1000))
print(final_price_after_gst(1000, 10))