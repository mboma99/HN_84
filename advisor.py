import streamlit as st
from datetime import datetime, date, timedelta
import yfinance as yf
import pandas as pd
import plotly.graph_objs as go
import openai

START = "1900-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

st.title('Bot4Stock')

st.markdown(
    "Finance advice at your fingertips."
)

st.markdown(
    "**Disclaimer:** This app is for informational purposes only and should not solely be used for making investment decisions. Always consult with a real qualified financial advisor before making investment choices."
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

    user_input = st.text_area('Chat with the Chat Bot', height=75)

    openai.api_key = ""

    def chat_with_bot(user_input):
        if user_input:
            response = openai.Completion.create(
                engine="davinci",
                prompt=user_input,
                max_tokens=50  
            )
            return response.choices[0].text
        return ""

    bot_response = chat_with_bot(user_input)
    if bot_response:
        st.write("Chat Bot:", bot_response) 
