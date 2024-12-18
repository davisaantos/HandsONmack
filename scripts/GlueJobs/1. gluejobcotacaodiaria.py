import yfinance as yf
import pandas as pd

#Função genérica para leitura da ultima cotação disponivel
def get_cotacao (ativo):
    cotacao = yf.Ticker(ativo)
    lst = cotacao.history(period="1d", interval="1d")
    return lst

#Recupera todos os ativos componenetes do indice nasdaq-100
#https://www.slickcharts.com/nasdaq100

df_ativo = pd.read_csv('s3://carteiracotacoes/nasdaq-100.csv',delimiter=';')
df_ativo.head()

#recupera a cotação de todos ativos

df_ativo = df_ativo.reset_index()
df_cotacao = pd.DataFrame(columns=['Date', 'Ativo', 'ValorFechamento'])

for index, row in df_ativo.iterrows():
    df_valor = get_cotacao (row['Symbol'])
    df_valor = df_valor.reset_index()

    # Adiciona nova linha
    df_cotacao.loc[len(df_cotacao)] = [row['Symbol'], df_valor.iloc[0]['Date'], df_valor.iloc[0]['Close']]
    print(df_cotacao.loc[len(df_cotacao)-1])

#Grava cotações atualizadas

df_cotacao = df_cotacao.reset_index()
df_cotacao.columns = ["id", "CodigoAtivo", "DataFechametno", "ValorFechamento"] # Use the columns attribute to rename columns.
df_cotacao.head()
df_cotacao.to_csv('s3://carteiracotacoes/cotacao.csv')