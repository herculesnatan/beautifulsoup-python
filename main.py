import requests
from bs4 import BeautifulSoup

link = 'https://www.google.com/search?q=cota%C3%A7%C3%A3o+do+dolar'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}

requisicao = requests.get(link, headers=headers)
print(requisicao)
site = BeautifulSoup(requisicao.text, 'html.parser')

# print(site.prettify())
titulo = site.find('title')
# print(titulo)

pesquisa = site.find_all('input')
#print(pesquisa[1])

cotacao_dolar = site.find('span',class_ = 'SwHCTb')
print(cotacao_dolar["data-value"])

print(cotacao_dolar.get_text())