import streamlit as st 
import requests 


def main(): 
    st.title("A text classification UI: Which type of negative content is your comment?")

    text_input = st.text_input("Enter a comment: ")


    response = requests.post(f"http://127.0.0.1:8000/classify?text={text_input}")
    data = response.json()

    st.write("The corresponding label:", data)

if __name__ == '__main__': 
    main()



