import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

url = "https://g1.globo.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

titulo = soup.find_all('div', class_='_evt')

textos = [m.text.strip() for m in titulo]

for titulo in textos:
    print(titulo)

