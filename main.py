import streamlit as st 

from langchain_groq import ChatGroq
from dotenv import load_dotenv


load_dotenv()

def load_answer(question):

    llm = ChatGroq(model="llama-3.1-8b-instant")
    answer = llm.invoke(question)
    return answer

#App UI starts here
st.set_page_config(page_title="Streamlit LKangchain Demo", page_icon=":robot:")
st.header("Streamlist Langchain Demo")

def get_text():
    input_text = st.text_input("You: ", key="input")
    return input_text

user_input = get_text()
response = load_answer(user_input)

submit = st.button('Generate')

if submit:
    st.subheader("Answer: ")
    st.write(response.content)