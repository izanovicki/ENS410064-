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


# Extrair as estatísticas de thetao
thetao_stats = df['thetao'].describe()

# Exibir as respostas de forma clara
media = thetao_stats['mean']
percentil_50 = thetao_stats['50%']
percentil_25 = thetao_stats['25%']
percentil_75 = thetao_stats['75%']

# Exibir as respostas formatadas
print(f"(a) A média da série de dados (thetao) é: {media:.3f}°C")
print(f"(b) O valor do meio (percentil 50%) é: {percentil_50:.3f}°C")
print(f"(c) A faixa de valores entre os percentis 25% e 75% é: {percentil_25:.3f}°C a {percentil_75:.3f}°C")