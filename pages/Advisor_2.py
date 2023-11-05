import streamlit as st
import os as os
from langchain.llms import OpenAI
from apikey import apikey
from SearchWeb import SearchWeb
import pandas as pd

st.title('Stock Advisor')

stocks = pd.read_csv("nasdaq.csv")
stocks_symbols = stocks["Symbol"].tolist()

stocks_input = st.text_input(
    'Enter stock symbol:'
)

selected_stocks = [
    symbol.strip().upper()
    for symbol in stocks_input.split(',')
    if symbol.strip().upper() in stocks_symbols
]

if not selected_stocks:
    st.warning('Please enter a valid stock symbol.')

else:
    os.environ['OPENAI_API_KEY'] = apikey
    llm = OpenAI(temperature=0.9)

    searches = SearchWeb()
    links = []
    for symbols in selected_stocks:
        links = searches.getResults(f"Latest {symbols} news")
        st.header(f"Check out {symbols}'s latest news")
        for link in links:
            st.write(link)





    #st.write("AI Genies insights")


   # st.write(llm(f'give brief insight of the {symbol}'))


    #prompt = st.text_area('Chat with the Chat Bot', height=75)
    #if prompt:
    #    response = llm(prompt)
    #    st.write(response)
