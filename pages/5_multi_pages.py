import streamlit as st


def multi_page():
    st.write()
    """
    # E. Divide application to different pages
    
    ## 1. 基础用法
    
    - 用 `st.Page(page, title, url_path, icon)` 来创建页面对象。
    - 用 `pg = st.navigation(page_list)` 来创建 navigator。
    - 用 `pg.run()` 来显示页面内容。

    ## 2. 页面框架：创建共用页眉和页脚
    
    入口文件中的`pg.run()`是页面内容显示的位置，其他部分可以通过代码创建元素来形成页面框架。
    因此，我们可以通过在`pg.run()`代码的前后来添加代码的方式来编写页面公用的框架，例如共用页眉和页脚！
    
    ## 3. 手动设置页面标题和图标
    
    `st.set_page_config()`可以用来手动设置页面的标题和图标，但是必须在`st.navigation`之后执行。此外，该函数可以在入口文件，或任意一个页面文件中执行。
    
    ## 4. 哪些东西会在页面之间共享？
    
    - 每个页面会共享使用python库，例如库中的全局变量如果被修改，其他地方用到这个变量时就是修改后的变量。
    - 每个页面共享Session State中的数据。
    - 入口文件中创建的元素，在每个页面中都可见。
    
    ## 5. 学会使用session state
    
    在session state被清楚之前，我们可以通过以下代码将前一个session state中的数据保留到当前的新session state中来：
    
    ```python
    if 'my_key' in st.session_state:
        st.session_state.my_key = st.session_state.my_key
    ```
    """


if __name__ == "__main__":
    multi_page()
