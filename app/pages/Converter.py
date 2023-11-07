import streamlit as st
from datetime import date
import yfinance as yf

TODAY = date.today().strftime("%Y-%m-%d")

st.title('Stock Price and Share Amount Converter')

st.markdown(
    "**Disclaimer:** This app is for informational purposes only and should not be used for making investment decisions. Always consult with a qualified financial advisor before making investment choices."
)

stock_symbol = st.text_input('Enter Stock Symbol', '')
number_of_shares = st.number_input('Enter Number of Shares', min_value=0.0, step=0.01)
selected_date = st.date_input('Select a date', date.today())

if not stock_symbol:
    st.warning('Please enter a valid stock symbol.')
elif number_of_shares <= 0:
    st.warning('Please enter a valid number of shares.')
else:
    data_load_state = st.text('Loading data...')

    data = yf.download(stock_symbol, selected_date.strftime("%Y-%m-%d"), TODAY)

    if data.empty:
        st.warning(f'No data available for {stock_symbol} on the selected date.')
    else:
        st.write(f'{stock_symbol} Historical Stock Prices:')
        st.write(data)

        latest_stock_price = data['Close'].iloc[-1]
        total_stock_price = latest_stock_price * number_of_shares

        st.write(f'Total Stock Price for {number_of_shares} shares of {stock_symbol}: ${total_stock_price:.2f}')

    data_load_state.text('Loading data... done!')
