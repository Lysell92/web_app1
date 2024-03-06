import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)




st.title("My to-do App")
st.subheader("This is a to-do app.")
st.write("This app keeps an overview of things to-do")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"todos_{index}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"todos_{index}"]
        st.experimental_rerun()



st.text_input(label="Enter a todo", placeholder="Add new todo...",
              on_change=add_todo, key ="new_todo")







































