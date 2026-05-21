# =========================================================
# STREAMLIT FUNDAMENTALS + INPUT WIDGETS
# =========================================================

# Import Streamlit library
import streamlit as st

# Import pandas for data handling
import pandas as pd
st.write("Hello World")

# Main title of the application
st.title("Streamlit Application")

# Display normal text
st.write("This is my First Streamlit App")

# Header (medium-sized heading)
st.header("Welcome to Streamlit")

# Subheader (smaller than header)
st.subheader("This is subheader")

# Plain text output
# Useful for logs and simple messages
st.text("This is plain text")



# =========================================================
# MARKDOWN
# =========================================================

# Markdown supports formatting like:
# bold, italic, bullet points, code blocks, etc.

st.markdown("## Markdown Section")

st.markdown("""
### Features of Streamlit
- Easy to learn
- Fast development
- Python based
- Great for dashboards
""")

# Bold text
st.markdown("**This is bold text**")

# Italic text
st.markdown("*This is italic text*")

# Button 

if st.button("Click me"):
    st.write("Button Clicked")

agree = st.checkbox('I agree')
if agree:
    st.write("You agreed!")

level = st.slider('Select a level:', 1, 10 ,5)
st.write(f"Selected level is {level}")

uploaded_file = st.file_uploader('Upload a File', type=["csv", "txt", 'pdf'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

#-------------------------------------DETAILED NOTES--------------------------------------------


# =========================================================
# BASIC OUTPUT FUNCTIONS
# =========================================================

# st.write() is the most flexible display function
# It can display text, variables, tables, lists, etc.
st.write("Hello World")


# Main title of the application
st.title("Streamlit Application")


# Display normal text
st.write("This is my First Streamlit App")


# Header (medium-sized heading)
st.header("Welcome to Streamlit")


# Subheader (smaller than header)
st.subheader("This is subheader")


# Plain text output
# Useful for logs and simple messages
st.text("This is plain text")


# =========================================================
# MARKDOWN
# =========================================================

# Markdown supports formatting like:
# bold, italic, bullet points, code blocks, etc.

st.markdown("## Markdown Section")

st.markdown("""
### Features of Streamlit
- Easy to learn
- Fast development
- Python based
- Great for dashboards
""")

# Bold text
st.markdown("**This is bold text**")

# Italic text
st.markdown("*This is italic text*")


# =========================================================
# CODE DISPLAY
# =========================================================

# Display formatted code with syntax highlighting

sample_code = '''
def add(a, b):
    return a + b
'''

st.code(sample_code, language="python")


# =========================================================
# JSON DISPLAY
# =========================================================

# Display dictionary in JSON format

student = {
    "name": "Arun",
    "age": 22,
    "skills": ["Python", "Streamlit"]
}

st.json(student)


# =========================================================
# BUTTON WIDGET
# =========================================================

# st.button() returns True when clicked

if st.button("Click me"):

    # This code runs only when button is clicked
    st.write("Button Clicked")


# =========================================================
# CHECKBOX WIDGET
# =========================================================

# Checkbox returns True or False

agree = st.checkbox("I agree")

if agree:

    st.write("You agreed!")


# =========================================================
# SLIDER WIDGET
# =========================================================

# Slider allows selecting numeric values

level = st.slider(
    "Select a level:",
    1,      # minimum value
    10,     # maximum value
    5       # default value
)

# Display selected slider value
st.write(f"Selected level is {level}")


# =========================================================
# TEXT INPUT
# =========================================================

# Text input for user typing

name = st.text_input(
    "Enter your name"
)

# Check if user entered something
if name:

    st.write(f"Hello {name}")


# =========================================================
# NUMBER INPUT
# =========================================================

# Accept numeric input only

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100,
    step=1
)

st.write(f"Your age is {age}")


# =========================================================
# SELECTBOX
# =========================================================

# Dropdown selection widget

language = st.selectbox(
    "Choose Programming Language",
    ["Python", "Java", "C++", "JavaScript"]
)

st.write(f"Selected language: {language}")


# =========================================================
# RADIO BUTTON
# =========================================================

# Radio buttons allow selecting one option

gender = st.radio(
    "Select Gender",
    ["Male", "Female", "Other"]
)

st.write(f"Selected Gender: {gender}")


# =========================================================
# MULTISELECT
# =========================================================

# Allows selecting multiple options

skills = st.multiselect(
    "Select Skills",
    ["Python", "Django", "Flask", "Streamlit"]
)

st.write("Selected Skills:", skills)


# =========================================================
# FILE UPLOADER
# =========================================================

# Upload files from local computer

uploaded_file = st.file_uploader(
    "Upload a File",
    type=["csv", "txt", "pdf"]
)


# Check if file is uploaded
if uploaded_file is not None:

    # Display uploaded file name
    st.write("Uploaded File:", uploaded_file.name)

    # Read CSV files using pandas
    if uploaded_file.name.endswith(".csv"):

        # Convert uploaded CSV into DataFrame
        df = pd.read_csv(uploaded_file)

        # Display first 5 rows
        st.write("Preview of Uploaded CSV")

        st.dataframe(df.head())


# =========================================================
# DATAFRAME DISPLAY
# =========================================================

# Create sample DataFrame

data = {
    "Name": ["Arun", "Rahul", "Aman"],
    "Marks": [90, 85, 88]
}

df = pd.DataFrame(data)

# Interactive table
st.dataframe(df)


# Static table
st.table(df)


# =========================================================
# METRICS
# =========================================================

# KPI-style display

st.metric(
    label="Revenue",
    value="$5000",
    delta="+10%"
)


# =========================================================
# SIDEBAR
# =========================================================

# Sidebar content appears on left side

st.sidebar.title("Sidebar Menu")

page = st.sidebar.selectbox(
    "Choose Page",
    ["Home", "Profile", "Settings"]
)

st.sidebar.write(f"Selected Page: {page}")


# =========================================================
# COLUMNS
# =========================================================

# Create horizontal layout

col1, col2 = st.columns(2)

with col1:

    st.header("Column 1")
    st.write("This is left column")

with col2:

    st.header("Column 2")
    st.write("This is right column")


# =========================================================
# TABS
# =========================================================

# Organize content into tabs

tab1, tab2 = st.tabs(["Python", "Java"])

with tab1:

    st.write("Python Content")

with tab2:

    st.write("Java Content")


# =========================================================
# EXPANDER
# =========================================================

# Hidden collapsible section

with st.expander("See More Details"):

    st.write("""
    Streamlit is an open-source Python library
    used to build web applications quickly.
    """)


# =========================================================
# SESSION STATE
# =========================================================

# Store values across reruns

if "counter" not in st.session_state:

    st.session_state["counter"] = 0


# Increment counter
if st.button("Increase Counter"):

    st.session_state["counter"] += 1


# Display counter value
st.write("Counter Value:", st.session_state["counter"])


# =========================================================
# SUCCESS / ERROR / WARNING MESSAGES
# =========================================================

st.success("Success Message")

st.warning("Warning Message")

st.error("Error Message")

st.info("Information Message")


# =========================================================
# END OF APPLICATION
# =========================================================

st.write("Application Finished Successfully")   