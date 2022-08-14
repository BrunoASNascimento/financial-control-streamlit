import streamlit as st


def main():
    st.sidebar.title("Sidebar")
    page_selected = st.sidebar.selectbox(
        "Pagina",
        ["Dashboard"]
    )
    if page_selected == "Dashboard":
        st.title("Dashboard")
        st.write("Hello World")
    else:
        st.title("Page not found")


if __name__ == '__main__':
    main()
