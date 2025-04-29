import streamlit as st


def widgets():
    """
    # B. Widgets

    ## 1. st.slider()
    """

    x = st.slider("x")  # 👈 this is a widget
    f"{x} squared is {x**2}"

    "## 2. st.text_input()"

    st.text_input("Your name", key="name")

    # You can access the value at any point with:
    f"name: {st.session_state.name} (visit from `st.session_state`)"

    "## 3. st.checkbox()"

    flag = st.checkbox("Show dataframe")
    if flag:
        "checkbox: True"
    else:
        "checkbox: False"

    "## 4. st.selectbox()"

    option = st.selectbox(
        "Which number do you like best?", ["Apple", "Banana", "Cherry"]
    )

    f"You selected: {option}"


if __name__ == "__main__":
    widgets()
