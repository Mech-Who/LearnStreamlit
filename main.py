import streamlit as st

routes = {
    # Define the pages
    "basic": [
        {
            "page": "pages/1_basic_functions.py",
            "title": "1. Basic Functions",
            "url_path": "/functions",
            "icon": "🎈",
        },
        {
            "page": "pages/2_widgets.py",
            "title": "2. Common Widgets",
            "url_path": "/widgets",
            "icon": "❄️",
        },
        {
            "page": "pages/3_layouts.py",
            "title": "3. Common Layouts",
            "url_path": "/layouts",
            "icon": "🎉",
        },
        {
            "page": "pages/4_advanced.py",
            "title": "4. Advanced Concepts",
            "url_path": "/advanced",
            "icon": "🎈",
        },
    ],
    "Multi Pages": [
        {
            "page": "pages/5_multi_pages.py",
            "title": "5. Multi-page Application",
            "url_path": "/multi_pages",
            "icon": "❄️",
        },
    ],
    "Static Resources": [
        {
            "page": "pages/6_static_resources.py",
            "title": "6. Static Resources",
            "url_path": "/static_resources",
            "icon": "🎉",
        },
    ],
}


def main():
    # apply to every page
    st.sidebar.button("Show on every page!")

    """
    # 页眉
    
    梦开始的地方！
    ![宋雨琦](http://localhost:8501/app/static/syq_hd.jpg)
    ---
    
    st.navigation(pages, *, position="sidebar", expanded=False)
    
    - pages: List[st.Page|str]|Dict[str, st.Page|str], 应用程序的可用页面。页面对象只能是st.Page对象或者page的路径。如果需要自定义页面的标题等信息，则必须使用st.Page
    - position: str, 导航菜单的位置。如果这是 "sidebar" （默认），则导航 Widget 将显示在侧边栏的顶部。如果 this is "hidden" ，则不显示 Navigation Widget。如果pages只有一个页面，则此选项失效，且不会显示导航菜单。
    - expanded: bool, 是否应展开导航菜单。如果这是 False （默认），导航菜单将折叠并包含一个 按钮可在要显示的页面过多时查看更多选项。 如果为 True ，则导航菜单将始终展开;不会显示折叠菜单的按钮。
    """

    # Set up navigation
    pg = st.navigation(
        {
            dir_name: [st.Page(**page) for page in pages]
            for dir_name, pages in routes.items()
        }
    )
    # Run the selected page
    pg.run()

    """
    ---
    
    # 页脚
    
    只要当前作用域中使用了st，就可以通过直接写文本的方式来写markdown，无需通过`st.write()`函数来写固定的markdown文本(格式化字符串也可以）！因此，可以通过以下方式来快速编写页面内容：
    ```python
    # new_page.py
    import streamlit as st
    
    def page_name():
        st.write()
        \"\"\"
        # 页面标题
        
        各种Markdown文字
        一些文字
        \"\"\"
        
    if __name__j == "__main__":
        page_name()
    ```
    """


if __name__ == "__main__":
    main()
