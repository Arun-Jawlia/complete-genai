import streamlit as st

if "count" not in st.session_state:
    st.session_state['count'] = 0

st.title("Counter App for learning Session state")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Increase"):
        st.session_state['count'] += 1

with col2:
    if st.button("Decrease"):
        st.session_state['count'] -= 1

with col3:
    if st.button("Reset"):
        st.session_state['count'] = 0

st.header(f"Count: {st.session_state['count']}")