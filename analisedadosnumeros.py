import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import lxml

url = "https://pt.wikipedia.org/wiki/Lista_de_unidades_federativas_do_Brasil_por_popula%C3%A7%C3%A3o"

tabelas = pd.read_html(url)

#print(len(tabelas))
#print(tabelas[1].head())

df = pd.read_html(url)[1]

#print(df.head())
#print(df.columns)

df.columns.get_level_values(0)
df.columns.get_level_values(1)

print(df.columns.get_level_values(0).unique())
print(df.columns.get_level_values(1).unique())
print(df.columns.get_level_values(0).unique()[0])
print(df.columns.get_level_values(1).unique()[0])
print(df.columns.get_level_values(0).unique()[1])
print(df.columns.get_level_values(1).unique()[1])




