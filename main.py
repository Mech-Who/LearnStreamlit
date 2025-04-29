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
    
    ---
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
    # new_file.py
    import streamlit as st
    
    def page_name():
        st.write()
        "# 页面标题"
        <字符串>
        "一些文字"
        "由于这里无法使用三引号来写，因此只能一行一行写"
        
    if __name__j == "__main__":
        page_name()
    ```
    """


if __name__ == "__main__":
    main()
