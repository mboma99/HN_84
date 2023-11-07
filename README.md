# HN_84
Nottingham 2023 hackerthon

project demo : https://youtu.be/QE2MULe5E5g

# Bot4Stock
An app designed to provide financial literacy on stocks through visualising, converting and advising based on Stock Performances.

## Overview
This compact application acts as an online financial toolkit designed and engineered using Python and Streamlit. This provides insight on stock finance on a multitude of ways, with the use of yFinance to retrieve financial data. 

Firstly, it can visualise historical stock performances using Plotly Graphs and Pandas Dataframes over a user-inputted timeframe through the "Visualiser" page.

Secondly, it can provide the estimated share price of a stock, providing the value of your stock shares through the "Converter" page.

Finally, it can provide financial insight about your chosen stock through the use of a Chatbot powered by OpenAI. In addition, through the use of a web scraper using SerpAPI, the program can return relevant articles talking about the stock. This is in the "Advisor" page

## Docker Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/mboma99/HN_84.git
   ```

2. **Go to app folder in cli**
   ```
   cd HN_84\app
   ```

4. **Build Docker Image**
   ```
   docker compose up --build
   ```
## Manual Installation

1. **Clone the repository:**

   ```
   git clone https://github.com/mboma99/HN_84.git
   ```
   
2. **Create a virtual environment (venv):**

   ```
   python -m venv venv
3. **Activate the virtual environment:**

   On Windows:
   ```
   venv\Scripts\activate
   
   or
   
   source venv/bin/activate
4. **Install the required Python packages:**
   ```
   pip install -r requirements.txt
5. Run the Streamlit app:
   ```
   streamlit run Home.py
Access the application:
Open your web browser and go to http://localhost:8501 to use the application.

Usage:
Enter stock symbols (comma-separated) in the input field.
Input start and end date to view the historical stock price data in interactive graphs in the "Visualisation" page.
Input share amount to view the value of your shares in the "Conversion" page.
Input your stock to use the provided bot to gain insight and article links about relevant information regarding the stock in the "Advisor" page.

## This project was done as a collaboration for HackNotts84.
### Collaborators:
Harry Nguyen - https://github.com/htqn2005
James Mboma - https://github.com/mboma99
