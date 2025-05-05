import streamlit as st


def widgets():
    """
    # B. Widgets

    ## 1. st.slider()
    """

    x = st.slider("x")  # 👈 this is a widget
    f"{x} squared is {x**2}"

    """
    ## 2. st.text_input()
    
    st.text_input(label, value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible", icon=None)
    
    - label: str, 一个简短的标签，向用户说明此输入的用途。标签可以选择包含以下类型的 GitHub 风格的 Markdown：粗体、斜体、删除线、内联代码、链接和图像。图像的显示方式与图标类似，最大高度等于字体高度。label不应该为空，如果不想展示，可以通过label_visibility进行设置。
    - value: object, 此 widget 首次呈现时的文本值。这将在内部转换为 str 。如果为 None ，则初始化为空并返回 None ，直到用户提供输入。默认为空字符串。
    - max_chars: int, 文本输入中允许的最大字符数。
    - key: str|int, 用作小组件的唯一键的可选字符串或整数。如果省略此项，则将根据 Widget 的内容为 Widget 生成一个键。没有两个 widget 可以具有相同的键。
    - type: str, 文本输入的类型。这可以是 “default” （对于常规文本输入） 或 “password” （对于屏蔽用户键入的值的文本输入）。默认为 “default”。
    - help: str, 显示在 Widget 标签旁边的工具提示。Streamlit 仅在 时 label_visibility="visible" 显示工具提示。如果为 None （default），则不显示工具提示。
    - autocomplete: str, 将传递给 <input> 元素的 autocomplete 属性的可选值。如果未指定，则对于“password”输入，此值将设置为“new-password”，对于“default”输入，此值将设置为空字符串。有关更多详细信息，请参阅 https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/autocomplete
    - on_change: function, 此文本输入的值更改时调用的可选回调
    - args: Tuple, 要传递给回调的可选 args 元组。
    - kwargs: Dict, 要传递给回调的可选 kwargs dict。
    - placeholder: str, 文本输入为空时显示的可选字符串。如果为 None，则不显示任何文本。
    - disabled: bool, 如果设置为 True 则禁用输入。默认为 False 。
    - label_visibility: str, 标签的可见性。默认值为 "visible" .如果为 "hidden" ，则 Streamlit 将显示一个空分隔条而不是标签，这有助于使 Widget 与其他 Widget 保持一致。
    - icon: str, 一个可选的表情符号或图标，显示在值左侧的输入字段中。如果为 icon is None （默认），则不显示图标。如果 icon 是字符串，则以下选项有效：单字符表情符号（如🚨、🔥）;材质符号库中的图标（圆角样式）（如`:material/icon_name:`、`:material/thumb_up:`）
    """

    st.text_input("你的名字：", key="name")

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

    """
    ## 5. st.button()
    
    st.button(label, key=None, help=None, on_click=None, args=None, kwargs=None, *, type="secondary", icon=None, disabled=False, use_container_width=False)
    
    - label: str, 一个简短的标签，向用户说明此按钮的用途。标签可以选择包含以下类型的 GitHub 风格的 Markdown：粗体、斜体、删除线、内联代码、链接和图像。图像的显示方式与图标类似，最大高度等于字体高度。
    - key: str|int, 用作小组件的唯一键的可选字符串或整数。如果省略此项，则将根据 Widget 的内容为 Widget 生成一个键。没有两个 widget 可以具有相同的键。
    - help: str, 将鼠标悬停在按钮上时显示的工具提示。如果为 None （default），则不显示工具提示。工具提示可以选择包含 GitHub 风格的 Markdown，包括 body 的参数。
    - on_click: function，回调函数，单击按钮时执行
    - args: Tuple, 传递给回调函数的参数元组
    - kwargs: Dict, 传递给回调函数的参数字典
    - type: str, 指定按钮类型的可选字符串("primary", "secondary", "tertiary")。
    - icon: str, 显示在按钮标签旁边的可选表情符号或图标。如果 icon is None （默认），则不显示任何图标。如果 icon 是字符串，则以下选项有效：单字符表情符号（如🚨、🔥）;材质符号库中的图标（圆角样式）（如`:material/icon_name:`、`:material/thumb_up:`）
    - disabled: bool, 一个可选布尔值，如果设置为 True ，则禁用按钮。默认值为 False .
    - use_container_width是否扩展按钮的宽度以填充其父容器。如果为 use_container_width is False （默认），则 Streamlit 调整按钮的大小以适合其内容。如果 use_container_width 是 True ，则按钮的宽度与其父容器匹配。在这两种情况下，如果按钮的内容比父容器宽，则内容将换行。
    
    返回值：如果在上次运行应用程序时单击该按钮，则为 True，否则为 False。
    """
    st.button("Click", key=1, help="Just for test", type="primary", icon="🔥")


if __name__ == "__main__":
    widgets()
