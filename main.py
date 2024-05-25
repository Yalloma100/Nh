# main.py
import streamlit as st

def main():
    st.title("Мій перший додаток Streamlit")
    user_name = st.text_input("Як вас звати?")
    if user_name:
        st.write(f"Привіт, {user_name}!")

if __name__ == "__main__":
    main()
  
