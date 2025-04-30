import streamlit as st


def layout():
    st.write()
    """
    # C. Layout

    ## 1. add selectbox to sidebar

    `add_selectbox = st.sidebar.selectbox(tips, option_list)`
    """
    # Add a selectbox to the sidebar:
    add_selectbox = st.sidebar.selectbox(
        "How would you like to be contacted?", ("Email", "Home phone", "Mobile phone")
    )

    """
    ## 2. add slider to sidebar
    
    `add_selectbox = st.sidebar.slider(tips, start, end, value_list)`
    """
    # Add a slider to the sidebar:
    add_slider = st.sidebar.slider("Select a range of values", 0.0, 100.0, (25.0, 75.0))

    """
    ## 3. add different widgets in same column as content
    
    create by: `left_column, right_column = st.columns(2)`
    """
    left_column, right_column = st.columns(2)
    # You can use a column just like st.sidebar:
    left_column.button("set left column by: `left_column.button()`(create a button)")

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        "use right column by: `with right_column: chosen = st.radio(tips, option_list)` (use by function)"
        chosen = st.radio(
            "Sorting hat", ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin")
        )
        f"You are in {chosen} house!"

    "## 4. add progress bar"

    prog = st.slider("Set progress value", 0, 100, 0)
    # Add a placeholder

    "add placeholder by: `ph = st.empty()`, and update by: `ph.text(new_value)`"

    latest_iteration = st.empty()
    bar = st.progress(0)

    "create by: `bar = st.progress(0)`, update by: `bar.progress(value)`"

    latest_iteration.text(f"Progress: {prog}%")
    bar.progress(prog)


if __name__ == "__main__":
    layout()
