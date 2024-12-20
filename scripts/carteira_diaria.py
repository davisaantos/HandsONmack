# -*- coding: utf-8 -*-
"""carteira_diaria.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qzoOs4cqkcN0WoxGN2J7P8HyAyi5HZ-8
"""

#Declara bibliotecas
import pandas as pd

#Recupera todos os clientes

df_cliente = pd.read_csv('s3://carteiracotacoes/clientes.csv',delimiter=';')
df_cliente.head(10)

#Recupera todos as carteiras

df_carteira = pd.read_csv('s3://carteiracotacoes/carteira.csv',delimiter=';')
df_carteira.head(10)

#Recupera cotacao

df_cotacao = pd.read_csv('s3://carteiracotacoes/cotacao.csv',delimiter=',')
df_cotacao.head(10)

# Junção das tabelas
df_resultado = df_cliente.merge(df_carteira, on='idCliente', how='left')
df_resultado = df_resultado.merge(df_cotacao, on='CodigoAtivo', how='left')
df_resultado['ValorAtivo'] = df_resultado['QtdeAtivo'] * df_resultado['ValorFechamento']
df_resultado.head(10)

#sumarizar carteira

df_final = df_resultado.groupby(['idCliente', 'NomeCliente'])['ValorAtivo'].sum()

df_final.to_csv('s3://carteiracotacoes/final.csv')
df_final.head(10)