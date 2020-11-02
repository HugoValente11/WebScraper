from bs4 import BeautifulSoup
import requests

search = input("What do you want to search?\n")
params = {"q" : search}
r = requests.get("https://www.bing.com/search", params = params)
soup = BeautifulSoup(r.text, "html.parser")
print(soup.prettify())

results = soup.find("ol", {"id": "b_results"})
links = results.find_all("li", {"class": "b_algo"})

for item in links:
    item_text = item.find("a").text
    item_link = item.find("a").attrs["href"]
    
    if item_text and item_link:
        print(item_text)
        print(item_link)

    