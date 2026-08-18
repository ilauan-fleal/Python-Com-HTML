import requests

from bs4 import BeautifulSoup

link_url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

x = requests.get(link_url)

site_html = x.text

k = BeautifulSoup(site_html, "html.parser")

todos_os_filmes = k.find_all(name="h3", class_="title")

print(todos_os_filmes)

filmes_titulos = [movie.getText() for movie in todos_os_filmes]

print(filmes_titulos)


filmes = filmes_titulos[::-1]

with open("movies.text", mode="w") as arquivo:
    for y in filmes:
        arquivo.write(f"{y}\n")