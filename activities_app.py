import json
import os
import streamlit as st
from datetime import datetime

TASK_FILE = "tasks.json"

# Load tasks from file
if os.path.exists(TASK_FILE):
    with open(TASK_FILE, "r") as file:
        tasks = json.load(file)
else:
    tasks = []

# Helper: Save tasks to file
def save_tasks():
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

# Streamlit UI
st.title("📝 To-Do List App")

# Add Task
with st.form("Add Task"):
    name = st.text_input("Task name")
    due_date = st.date_input("Due date")
    due_time = st.time_input("Due time")
    submitted = st.form_submit_button("Add Task")

    if submitted:
        tasks.append({
            "name": name,
            "completed": False,
            "due_date": due_date.strftime("%Y-%m-%d"),
            "due_time": due_time.strftime("%H:%M")
        })
        save_tasks()
        st.success(f"Task '{name}' added!")

# Display Tasks
st.subheader("Your Tasks")
for i, task in enumerate(tasks):
    col1, col2, col3 = st.columns([5, 2, 1])
    with col1:
        st.write(f"{task['name']} - Due: {task['due_date']} {task['due_time']}")
    with col2:
        if st.checkbox("Completed", key=f"comp_{i}", value=task["completed"]):
            task["completed"] = True
            save_tasks()
    with col3:
        if st.button("❌", key=f"del_{i}"):
            tasks.pop(i)
            save_tasks()
            st.experimental_rerun()
