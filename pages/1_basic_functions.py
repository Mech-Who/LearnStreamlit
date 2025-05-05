import cv2
import numpy as np
import pandas as pd
import streamlit as st


def read2RGB(path: str):
    img = cv2.imread(path)
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


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

    """
    ## 2. 展示图片

    st.image(img_or_path, captoin=None, width=None, clamp=False, channels="RGB", output_format="auto", *, use_container_width=False)
    
    - img_or_path: np.ndarray | str, 图像数据或图像的路径（包括相对路径和绝对路径）
    - caption: str, 图像的说明文字
    - width: int, 指定图像宽度，如果需要的话。
    - clamp: bool, 过滤图像数据的到[0, 255]
    - channels: str, 指定图像是RGB格式还是其他格式，默认是RGB
    - output_format: str, 指定图像读取方式 ("JPEG", "PNG", "auto"), 默认为auto
    - use_container_width: bool, 是否使用父容器的宽度进行覆盖 width 。
    """

    c11, c12, c13 = st.columns(3)
    img = read2RGB("static/syq_hd.jpg")
    c11.image("static/syq_hd.jpg", caption="宋雨琦1")
    c12.image(img, caption="宋雨琦2")
    c13.image(img, caption="宋雨琦3")

    c21, c22, c23 = st.columns(3)
    c21.button("宋1")
    c22.button("宋2")
    c23.button("宋3")


if __name__ == "__main__":
    basic_functions()
