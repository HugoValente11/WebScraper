from bs4 import BeautifulSoup
import requests

search = input("What do you want to search?\n")
params = {"q" : search}
r = requests.get("https://www.bing.com/search", params = params)
soup = BeautifulSoup(r.text)
print(soup.prettify())
