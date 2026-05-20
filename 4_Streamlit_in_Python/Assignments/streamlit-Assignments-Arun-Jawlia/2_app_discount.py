#  PRICE CALCULATOR 
import streamlit as st

st.title('Price Calculator')

price = st.number_input("Enter product price: ", min_value = 0.0 )

discount = st.slider("Enter discount %", min_value = 1, max_value = 50)

btn = st.button("Click to get Calculate Price")

if btn:
    final_price = price - ( price * discount) / 100

    st.success(f"Final Price: {final_price:.2f}")

    st.write("Original Price:", price)
    st.write("Discount:", f"{discount}%")
    st.write("Final Price:", final_price)

    table_data = [
        ["Before", price],
        ["After", final_price]
    ]

    st.table(table_data)
