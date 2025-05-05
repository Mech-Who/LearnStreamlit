import streamlit as st


def static_resources():
    st.write()
    """
    # F. Show static resources to user
    
    ## 1. 作为静态资源服务器使用
    
    Static resources normally can't be directly reached by users.
    However, we can make it happen:

    1. add config as follow to config file.
    ```toml
    # <project-dir>/.streamlit/config.toml
    [server]
        enableStaticServing = true
    ```
    2. place all the resources you want to be found to `static` folder in your project.
    3. visit these resources by url: `https://<streamlit_server>/app/static/<resources_filename>`
    """


if __name__ == "__main__":
    static_resources()
