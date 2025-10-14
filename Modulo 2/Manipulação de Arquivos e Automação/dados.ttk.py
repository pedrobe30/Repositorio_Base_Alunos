from bs4 import BeautifulSoup
import requests, os

url = "https://www.tiktok.com/login?redirect_url=https%3A%2F%2Fwww.tiktok.com%2F&lang=en&enter_method=mandatory"
resposta = requests.get(url)
conteudo_html = resposta.content

soup = BeautifulSoup(conteudo_html, 'html.parser')

fonte = soup.find_all('h2')

for h2 in fonte:
    print("Texto: {%s}, URL: {%s}" % (h2.text, h2.get('href')))