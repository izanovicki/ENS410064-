#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 15:23:35 2024

@author: isabele
"""

# Importar as bibliotecas necessárias
import xarray as xr
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carregar os dados do arquivo netCDF
ds = xr.open_dataset('/home/isabele/Documentos/Copernicus-data/Transecto-CF/Temperatura/temp200m-transecto-cf.nc')


# Visualizar as variáveis disponíveis no dataset
ds

# Escolher a variável desejada (substitua 'nome_da_variavel' pelo nome correto da variável)
data = ds['thetao']  # Substituir com a variável correta

# Converter para DataFrame do Pandas para análise
df = data.to_dataframe().reset_index()

# Analisar as estatísticas básicas da série temporal
stats = df.describe()

# Exibir as estatísticas
print (stats)

# Calcular a média e desvio padrão
mean = df['thetao'].mean()
std = df['thetao'].std()

# Plotar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(df['time'], df['thetao'], label='Dados originais')
plt.axhline(y=mean, color='r', linestyle='--', label='Média')
plt.fill_between(df['time'], mean - std, mean + std, color='gray', alpha=0.3, label='Desvio Padrão')

# Adicionar labels e legendas
plt.xlabel('Tempo')
plt.ylabel('Valor da variável')
plt.title('Gráfico de linha com média e desvio padrão')
plt.legend()
plt.show()

#(a) Qual a média da sua série de dados?

#A média da variável thetao (temperatura potencial) é 21,759°C.

#(b) Qual o valor do meio (percentil 50%)?

#O valor do meio (percentil 50%) para a variável thetao é 22,500°C.
#(c) Qual a faixa de valores entre os percentis 25% e 75%?

A faixa de valores entre o percentil 25% e 75% para thetao é de 19,944°C a 24,229°C.

