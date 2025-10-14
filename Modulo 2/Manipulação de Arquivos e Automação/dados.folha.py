from bs4 import BeautifulSoup
import requests, os

url = "https://www.folha.uol.com.br/"
resposta = requests.get(url)
conteudo_html = resposta.content

soup = BeautifulSoup(conteudo_html, 'html.parser')

paragrafos = soup.find_all('p')

for p in paragrafos:
    print("Texto: {%s}, URL: {%s}" % (p.text, p.get('href')))