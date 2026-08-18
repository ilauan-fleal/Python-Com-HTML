import requests
from bs4 import BeautifulSoup


x = requests.get("https://news.ycombinator.com/news")


pagina_web = x.text

y = BeautifulSoup(pagina_web,"html.parser")

print(y.title)

artigos_site = y.find_all(name="a", class_="storylink")

artigos_texto = []

artigos_link = []

for x in artigos_site:
    texto = x.getText()
    artigos_texto.append(texto)
    link = x.get("href")
    artigos_link.append(link)

artigos_votados = [int(score.getText().split()[0]) for score in y.find_all(name="span", class_="score")]

print(artigos_votados)