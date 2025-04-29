import streamlit as st


@st.cache_resource
def square_list(x):
    return x**2


@st.cache_data
def get_gender(name):
    male = ["Mike", "John"]  # can comes from database
    return "male" if name in male else "female"


def advance_concepts():
    st.write()
    """
    # D. Advance Concepts
    
    ## 1. Cache
    
    use cache by set decorator:
    
    1. `@st.cache_data` which can be store to database
    2. `@st.cache_resource` which cannot be store to database
    
    ## 2. Session state
    
    Session will renew if this page is refreshed!
    """

    if "counter" not in st.session_state:
        st.session_state.counter = 0
    st.session_state.counter += 1
    st.header(f"This page has run {st.session_state.counter} times.")
    st.button("Run it again")

    """
    ## 3. differences between cache and session_state
    
    1. Cache can be used for every user in every session.
    2. Session state can only be used by its own session.
    
    ## 4. Database connection
    
    ```python
    conn = st.connection('my_database')
    df = conn.query('select * from my_table')
    st.dataframe(df)
    ```
    
    Your connection config will be config at same dir with this py file, and named as `.streamlit/secrets.toml`
    Config content maybe like:
    
    ```python
    # <project-dir>/.streamlit/secrets.toml
    [connections.my_database]
        type="sql"
        dialect="mysql"
        username="xxx"
        password="xxx"
        host="example.com" # IP or URL
        port=3306 # Port number
        database='mydb' # Database name
    ```
    """


if __name__ == "__main__":
    advance_concepts()
