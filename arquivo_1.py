from bs4 import BeautifulSoup

with open("arquivo_1.html") as arquivo:
    conteudo = arquivo.read()

x = BeautifulSoup(conteudo, "html.parser")


tags_conjunto = x.find_all(name="p")


for y in tags_conjunto:
    print(y.getText())


secao_cabecalho = x.find(name="h1", class_="cabecalho")

print(secao_cabecalho)




cabecalhos_coletivos = x.select(".cabecalho")

print(cabecalhos_coletivos)