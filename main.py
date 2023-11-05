from SearchWeb import SearchWeb


searches = SearchWeb("latest apple news")

links = searches.getResults()

print(links)

