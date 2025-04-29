import numpy as np
import pandas as pd
import streamlit as st


def basic_functions():
    st.write("## 1. st.write()")
    df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
    st.write(df)

    st.write("## 2. st.dataframe()")
    dataframe = np.random.randn(10, 20)
    st.dataframe(dataframe)
    dataframe = pd.DataFrame(
        np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
    )

    st.write("### highlight_max")
    st.dataframe(dataframe.style.highlight_max(axis=0))

    st.write("## 3. st.table()")
    dataframe = pd.DataFrame(
        np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
    )
    st.table(dataframe)

    st.write("## 4. st.line_chart()")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

    st.write("## 5. st.map()")
    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
    )
    st.map(map_data)


def widgets():
    st.write("## 1. st.slider()")
    x = st.slider("x")  # 👈 this is a widget
    st.write(x, "squared is", x * x)

    st.write("## 2. st.text_input()")
    st.text_input("Your name", key="name")
    # You can access the value at any point with:
    st.write(f"name: {st.session_state.name} (visit from `st.session_state`)")

    st.write("## 3. st.checkbox()")
    flag = st.checkbox("Show dataframe")
    if flag:
        st.write("checkbox: True")
    else:
        st.write("checkbox: False")

    st.write("## 4. st.selectbox()")
    option = st.selectbox(
        "Which number do you like best?", ["Apple", "Banana", "Cherry"]
    )
    st.write(f"You selected: {option}")


def layout():
    st.write("## 1. add selectbox to sidebar")
    st.write("`add_selectbox = st.sidebar.selectbox(tips, option_list)`")
    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
    )

    st.write("## 2. add slider to sidebar")
    st.write("`add_selectbox = st.sidebar.slider(tips, start, end, value_list)`")
    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

    st.write("## 3. add different widgets in same column as content")
    st.write("create by: `left_column, right_column = st.columns(2)`")
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button("set left column by: `left_column.button()`(create a button)")

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        st.write(
            "use right column by: `with right_column: chosen = st.radio(tips, option_list)` (use by function)"
        )
        chosen = st.radio(
            "Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
        )
        st.write(f"You are in {chosen} house!")

    st.write("## 4. add progress bar")
    prog = st.slider("Set progress value", 0, 100, 0)
    # Add a placeholder
    st.write(
        "add placeholder by: `ph = st.empty()`, and update by: `ph.text(new_value)`"
    )
    latest_iteration = st.empty()
    bar = st.progress(0)
    st.write("create by: `bar = st.progress(0)`, update by: `bar.progress(value)`")
    latest_iteration.text(f"Progress: {prog}%")
    bar.progress(prog)


@st.cache_resource
def square_list(x):
    return x**2


@st.cache_data
def get_gender(name):
    male = ["Mike", "John"]  # can comes from database
    return "male" if name in male else "female"


def advance_concepts():
    st.write("## 1. Cache")
    st.write("use cache by set decorator:")
    st.write("1. `@st.cache_data` which can be store to database")
    st.write("2. `@st.cache_resource` which cannot be store to database")

    st.write("## 2. Session state")
    st.write("Session will renew if this page is refreshed!")
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    st.session_state.counter += 1
    st.header(f"This page has run {st.session_state.counter} times.")
    st.button("Run it again")

    st.write("## 3. differences between cache and session_state")
    st.write("1. Cache can be used for every user in every session.")
    st.write("2. Session state can only be used by its own session.")

    st.write("## 4. Database connection")
    st.write(
        "```python \nconn = st.connection('my_database') \ndf = conn.query('select * from my_table') \nst.dataframe(df) \n```"
    )
    st.write(
        "your connection config will be config at same dir with this py file, and named as `.streamlit/secrets.toml`"
    )
    st.write("Config content maybe like:")
    st.write("""
```python
[connections.my_database]
    type="sql"
    dialect="mysql"
    username="xxx"
    password="xxx"
    host="example.com" # IP or URL
    port=3306 # Port number
    database='mydb' # Database name
```
    """)


def main():
    st.write("# A. Basic functions")
    basic_functions()
    st.write("# B. Widgets")
    widgets()
    st.write("# C. Layout")
    layout()
    st.write("# D. Advance Concepts")
    advance_concepts()
    st.write("# E. Divide application to different pages")


if __name__ == "__main__":
    main()
