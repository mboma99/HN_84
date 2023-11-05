import requests
import streamlit as st
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.title("Bot4Stock")

st.markdown(
    "**Disclaimer:** This app is for informational purposes only and should not solely be used for making investment decisions. Always consult with a real qualified financial advisor before making investment choices."
)

st.markdown(
    "All prices will be in Dollars!"
)

lottie_hello = load_lottieurl("https://lottie.host/88817af3-ed84-46db-85c8-51930d9633fa/VCxcnO55bT.json")

st_lottie(
    lottie_hello,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", 
    key=None,
    height=200,  
    width=200,  
)

st.subheader("An app designed to provide financial literacy on stocks")
st.write("Includes a Advisor, Visualiser and Converter feature")

st.subheader('So what is Financial Literacy?')
lottie_man = load_lottieurl("https://lottie.host/9677787a-fa0b-4471-9df1-6da40320a2c3/rr8rgnuwYl.json")

st_lottie(
    lottie_man,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", 
    key=None,
    height=200,
    width=200,  
)

st.write("""
    Financial literacy is the ability to understand and effectively use various financial skills, such as budgeting, investing, and personal financial management. It is a lifelong journey of learning that empowers individuals to make informed financial decisions.
    Key aspects of financial literacy include budgeting, retirement planning, managing debt, and tracking personal spending.
""")

st.subheader('Why is Financial Literacy on Stocks important?') 

lottie_idea = load_lottieurl("https://lottie.host/e77827d5-50de-4cd2-b8f2-88374a79d979/5A8eQw7x9V.json")

st_lottie(
    lottie_idea,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", 
    key=None,
    height=200,
    width=200,  
)

st.write("""
    In modern society, financial literacy is crucial for managing day-to-day expenses, long-term financial planning, and avoiding financial pitfalls. Lacking financial literacy can lead to unsustainable debt, poor credit, bankruptcy, and other negative consequences.
    Financial literacy is essential for protecting individuals from financial fraud and achieving life goals, such as saving for education or retirement.
    """)

st.subheader('How this app helps you?')

lottie_money = load_lottieurl("https://lottie.host/3a6c7f0c-945a-4c53-8377-6a149db714b9/NQSPNU97gc.json")

st_lottie(
    lottie_money,
    speed=1,
    reverse=False,
    loop=True,
    quality="low",
    key=None,
    height=200,  
    width=200, 
)

st.write("""
    The app offers features like Stock Visualization, Share to Stock Conversion, and Stock Advisor to enhance financial literacy. Stock Visualization provides insights into stock performance, helping users make informed investment decisions. Share to Stock Conversion simplifies the process of converting shares. Stock Advisor offers expert guidance and recommendations. These features empower users 
    to make smarter financial choices and improve their financial well-being.
    """)

