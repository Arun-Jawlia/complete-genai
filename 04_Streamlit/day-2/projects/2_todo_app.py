import streamlit as st


st.set_page_config(page_title="Todo App", layout = 'centered')

if "tasks" not in st.session_state:
    st.session_state["tasks"] = []

st.title("Todo App")

st.sidebar.header("Task Statistics")

completed_count = sum(
    task["completed"]
    for task in st.session_state["tasks"]
)

st.sidebar.metric(
    "Total Tasks",
    len(st.session_state["tasks"])
)

st.sidebar.metric(
    "Completed Tasks",
    completed_count
)

st.header("Add New Task")

task_name = st.text_input("Enter Task")

priority = st.selectbox(
    "Select Priority",
    ["High", "Medium", "Low"]
)

# Category Dropdown
category = st.selectbox(
    "Select Category",
    [
        "Study",
        "Work",
        "Personal",
        "Health"
    ]
)

if st.button("Add Task"):
    if task_name: 
        st.session_state["tasks"].append({
            "name": task_name,
            "priority": priority,
            "category": category,
            "completed": False
        })
        st.success("Task Added Successfully")

st.divider()

st.header("Task Lists")

if not st.session_state['tasks']:
    st.info("No Tasks Added")

for index, task in enumerate(st.session_state['tasks']):
    col1, col2, col3, col4 = st.columns([4,2,2,1])

    with col1:
        completed = st.checkbox(
            task['name'],
            value = task['completed'],
            key=f"Check_{index}"
        )

        st.session_state['tasks'][index]['completed'] = completed
    
    with col2:

        st.write(
            f"🔥 {task['priority']}"
        )

    with col3:

        st.write(
            f"📂 {task['category']}"
        )

    with col4:

        if st.button("❌",key=f"delete_{index}"):
            st.session_state["tasks"].pop(index)

            st.rerun()