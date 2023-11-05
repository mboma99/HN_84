import os
import serpapi
from apikey import serp_apikey
from dotenv import load_dotenv
load_dotenv()

os.environ['SERPAPI_KEY'] = serp_apikey
api_key = os.getenv('SERPAPI_KEY')

client = serpapi.Client(api_key=api_key)
result = client.search(
	q="apple stock price",
	engine="google",
	location="United Kingdom",
	hl="en",
	gl="us",
	num = 5,
)
organic_results = result["organic_results"]
# Extract displayed links from the data
displayed_links = [entry['displayed_link'] for entry in organic_results]

# Print the extracted displayed links
for link in displayed_links:
    print(link)
