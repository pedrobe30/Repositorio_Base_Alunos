from bs4 import BeautifulSoup
import requests, os

url = "https://www.youtube.com/"
resposta = requests.get(url)
conteudo_html = resposta.content

soup = BeautifulSoup(conteudo_html, 'html.parser')

paragrafos = soup.find_all('a')

for p in paragrafos:
    print("Texto: {%s}, URL: {%s}" % (p.text, p.get('href')))