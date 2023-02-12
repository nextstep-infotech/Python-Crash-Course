from bs4 import BeautifulSoup
import requests


url = requests.get("https://dzone.com/articles/best-programming-jokes-amp-quotes").text

# print(url)

soup = BeautifulSoup(url,'lxml')

webpage_name = soup.title.string
# print(webpage_name)

ordered_list = soup.find("ol")
# print(ordered_list)

quotes_list = ordered_list.find_all("li")
# print(quotes_list)

with open("Quotes.txt", "w") as wf:
    for i,quote in enumerate(quotes_list,1):
        wf.write(str(i) + " " + quote.text)
        wf.write("\n")
