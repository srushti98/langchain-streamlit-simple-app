import streamlit as st

from langchain.schema import HumanMessage,SystemMessage,AIMessage
from langchain.chat_models import ChatOpenAI

st.set_page_config(page_title="Welcome to the Language Translator page")
st.header("Hey, Let's Translate")

chat=ChatOpenAI(temperature=0.6)

def get_chatmodel_response(from_lan,to_lan,question):
    messages = [
        SystemMessage(
            content="You are a helpful assistant that translates"+from_lan+"to"+to_lan+"."
        ),
        HumanMessage(
            content=question
        ),
    ]
    answer = chat(messages)

    return answer.content

from_lan = st.text_input("From language: ",key="l1")
to_lan = st.text_input("To language: ",key="l2")
input=st.text_input("Input: ",key="input")
response=get_chatmodel_response(from_lan,to_lan,input)

submit=st.button("Submit to translate")

if submit:
    st.subheader("The Response is")
    st.write(response)