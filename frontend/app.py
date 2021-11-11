import streamlit as st
import requests

session = requests.Session()
session.trust_env = False


def main():
    ########### Sidebar ##############################
    st.sidebar.markdown("# Docker compose app 🐳")
    st.header("Sum operation")
    a = float(st.text_input("Insert a", value=0))
    b = float(st.text_input("Insert b", value=0))
    button = st.button("Sum")
    query = {"a": a, "b": b}

    if button:
        response = requests.post("http://datascience_api:8080/add", params=query).json()
        st.write("a+b={}".format(response["result"]))


if __name__ == "__main__":
    main()
