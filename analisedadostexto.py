import requests # Importa a biblioteca requests para fazer requisições HTTP
from bs4 import BeautifulSoup # Importa a biblioteca BeautifulSoup para fazer parsing de HTML
import pandas as pd # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt # Importa a biblioteca matplotlib para visualização de dados
import seaborn as sns # Importa a biblioteca seaborn para visualização de dados
import numpy as np # Importa a biblioteca numpy para manipulação de arrays


resposta = requests.get("https://g1.globo.com/")


soup = BeautifulSoup(resposta.content, 'html.parser')

titulo = soup.find_all('div', class_='_evt')[1]

textos = [m.text.strip() for m in titulo]

for titulo in textos:
    print(titulo)

