import numpy as np
import pandas as pd
import streamlit as st


def basic_functions():
    st.write()
    """
    # A. Basic functions

    ## 1. st.write()
    """

    df = pd.DataFrame({"first column": [1, 2, 3, 4], "second column": [10, 20, 30, 40]})
    st.write(df)

    "## 2. st.dataframe()"

    dataframe = np.random.randn(10, 20)
    st.dataframe(dataframe)
    dataframe = pd.DataFrame(
        np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
    )

    "### highlight_max"

    st.dataframe(dataframe.style.highlight_max(axis=0))

    "## 3. st.table()"

    dataframe = pd.DataFrame(
        np.random.randn(10, 20), columns=("col %d" % i for i in range(20))
    )
    st.table(dataframe)

    "## 4. st.line_chart()"

    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
    st.line_chart(chart_data)

    "## 5. st.map()"

    map_data = pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4], columns=["lat", "lon"]
    )
    st.map(map_data)


if __name__ == "__main__":
    basic_functions()
