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
    
    st.columns(spec, *, gap="small", vertical_alignment="top", border=False)
    
    - spec: int|Tuple[float|int], 使用单个数字时，将创建相同大小的多个列，数字的值就是创建的列的个数；当使用Tuple或List的方式时，将按照数字呈现的关系来创建不同大小的多个列，数字的个数就是创建的列的个数
    - gap: str, 列之间的间隙大小，("small", "medium", "large")。默认值为 "small" 。
    - vertical_alignment: str, 列内内容的垂直对齐方式，("top", "center", "bottom")。默认值为 "top" .
    - border: bool, 是否在列容器周围显示边框。如果这是 False （默认），则不显示边框。如果为 True ，则每列周围会显示一个边框。
    
    创建两列：
    ```python
    left_column, right_column = st.columns(2)
    ```
    """
    left_column, right_column = st.columns(2, border=True)
    # You can use a column just like st.sidebar:
    with left_column:
        """
        创建按钮：
        ```python
        left_column.button()
        ```
        """
        if left_column.button("点一点"):
            "按下！"
        else:
            "松开！"

    # Or even better, call Streamlit functions inside a "with" block:
    with right_column:
        """
        以使用上下文管理的方式，创建单选框：
        ```python
        with right_column:
            chosen = st.radio(tips, option_list)
        ```
        """
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
