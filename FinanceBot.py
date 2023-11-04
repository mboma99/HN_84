import os
from apikey import apikey
import streamlit as st
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

#app framework

st.title('test gpt')
prompt = st.text_input('plug in prompt')

llm = OpenAI(temperature=0.9)

if prompt:
    response = llm(prompt)
    st.write(response)



