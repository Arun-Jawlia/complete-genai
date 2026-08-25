import streamlit as st

st.set_page_config(layout="wide")

st.title("Learning Layouts in Streamlit")

# Sidebar
st.sidebar.title("Sidebar Menu")

page = st.sidebar.selectbox(
    "Choose Page",
    ["Home", "Profile"]
)

# Columns
col1, col2 = st.columns(2)

with col1:
    st.header("Left Side")
    st.write("This is left column")

with col2:
    st.header("Right Side")
    st.write("This is right column")

# Tabs
tab1, tab2 = st.tabs(["Python", "Java"])

with tab1:
    st.write("Python Content")

with tab2:
    st.write("Java Content")

# Expander
with st.expander("See More"):
    st.write("This is a hidden Content ")