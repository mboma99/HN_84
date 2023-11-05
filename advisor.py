import streamlit as st
from datetime import datetime, date, timedelta
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
from langchain.llms import OpenAI
import os
from apikey import apikey
from SearchWeb import SearchWeb

START = "1900-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Bot4Stock')

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.sidebar.success("Select a mode above.")

st.markdown(
    "Finance advice at your fingertips."
)

st.markdown(
    "**Disclaimer:** This app is for informational purposes only and should not solely be used for making investment decisions. Always consult with a real qualified financial advisor before making investment choices."
)

st.markdown(
    "All prices will be in Dollars!"
)

stocks = pd.read_csv("nasdaq.csv")
stocks_symbols = stocks["Symbol"].tolist()

stocks_input = st.text_input(
    'Enter stock symbols (comma-separated)', ''
)
selected_stocks = [
    symbol.strip().upper()
    for symbol in stocks_input.split(',')
    if symbol.strip().upper() in stocks_symbols
]

if not selected_stocks:
    st.warning('Please enter at least one valid stock symbol.')
else:
    min_date = st.date_input(
        'Select a start date', datetime.strptime(START, "%Y-%m-%d")
    )
    max_date = st.date_input(
        'Select an end date', datetime.strptime(TODAY, "%Y-%m-%d")
    )

    data_load_state = st.text('Loading data...')

    historical_performance_fig = go.Figure()

    for symbol in selected_stocks:
        data = yf.download(
            symbol,
            min_date.strftime("%Y-%m-%d"),
            max_date.strftime("%Y-%m-%d"),
        )

        historical_performance_fig.add_trace(go.Scatter(x=data.index, y=data['Close'], mode='lines', name=f'{symbol} Historical Price'))

    historical_performance_fig.update_layout(
        title='Historical Performance of Selected Stocks',
        xaxis_title='Date',
        yaxis_title='Stock Price',
        template='plotly_dark'
    )

    st.plotly_chart(historical_performance_fig)

    data_load_state.text('Loading data... done!')

    for symbol in selected_stocks:
        st.write(f'{symbol} Historical Stock Prices:')
        st.write(data)

    #chatbot

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
