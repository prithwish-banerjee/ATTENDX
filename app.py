import streamlit as st

def main():
    st.header("This is header")
    name = st.text_input("Enter your name", key="name")
    if name:
        st.write(f"Hello, {name}!")
    st.button("Submit")

#     st.markdown("""


# """,allow_html=True)

main()