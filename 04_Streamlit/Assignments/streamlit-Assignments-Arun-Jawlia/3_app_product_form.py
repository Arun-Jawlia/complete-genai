# Product Form

import streamlit as st

st.title('Product Form')

product_name = st.sidebar.text_input("Enter Product Name")

category = st.sidebar.selectbox('Select Category:',["Electronices", "Camera", "Laptop", "Keyboard"])

price = st.sidebar.number_input("Enter Price")

btn = st.sidebar.button("Add Product")

if btn:
    st.success("Product Added")
    st.header("Product Detail")
    st.write('Product Name : ', product_name)
    st.write('Product Category : ', category)
    st.write('Product Price : ', price)