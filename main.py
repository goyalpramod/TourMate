import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
from dotenv import load_dotenv
import os
from chatbot import generate_message

with st.sidebar:
    st.title('🤗💬 Track 2 – LLM API Endpoint')
    st.markdown('''
    ## About
    This app is an LLM-powered and is built using the following technologies:
    - [Streamlit](https://streamlit.io/)
    - [LangChain](https://python.langchain.com/)
    - [OpenAI](https://platform.openai.com/docs/models) LLM model
 
    ''')
    add_vertical_space(5)
    st.write('Made with ❤️ by Praneetha, Gourav and Pramod')

 
def main():
    st.header("Make your travel plans with TourMate!")
    location = st.text_input("Where would you like to go?")
    duration = st.text_input("How long would you be staying there for")
    button_ind = st.button("*Generate Output*", type='secondary', help="Click to generate output based on information")
    if button_ind:
        output = generate_message(location,duration)
        st.write(output)

if __name__ == '__main__':
    main()