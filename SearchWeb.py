from bs4 import BeautifulSoup
import requests
import os
from apikey import serp_apikey
import serpapi
from apikey import serp_apikey
from dotenv import load_dotenv


class SearchWeb:

    def __init__(self):
        pass




    def getResults(self, search_prompt):
        os.environ['SERPAPI_KEY'] = serp_apikey
        api_key = os.getenv('SERPAPI_KEY')

        client = serpapi.Client(api_key=api_key)
        result = client.search(
            q=f"{search_prompt}",
            engine="google",
            location="United Kingdom",
            hl="en",
            gl="us",
            num=5,
        )
        organic_results = result["organic_results"]
        displayed_links = [entry['link'].split(' ')[0] for entry in organic_results]
        return displayed_links
