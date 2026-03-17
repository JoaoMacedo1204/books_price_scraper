#importa as bibliotecas para uso das requisicoes e comunicacao com o site
import requests
import pandas as pd
from bs4 import BeautifulSoup

#cria uma variavel para o uso do url
url = "https://books.toscrape.com/"

#verifica a requisicao do site
resposta = requests.get(url)
resposta.encoding = "utf-8"

#organiza a estrutura do texto do site no formato do HTML
site = BeautifulSoup(resposta.text, "html.parser")

#guarda as informacoes dos produtos na variavel
informacoes = site.find_all("article", class_="product_pod")

#lista vazia para receber o titulo e o preco dos livros
livros = []

#cria um laço de repeticao para a busca de titulos e precos
for busca in informacoes:
  titulo = busca.h3.a["title"]
  preco = busca.find("p", class_="price_color").text
  preco = preco.replace("£", "").strip()
  preco = float(preco)
  #insere os valores dentro da lista
  livros.append({
      "titulo": (titulo),
      "preco": (preco)
  })

#transforma a lista num Dataframe e uma planilha .csv
df = pd.DataFrame(livros)
df.to_csv('livros.csv', index=False)