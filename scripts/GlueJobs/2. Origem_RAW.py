import boto3
from pyspark.sql import functions as F
from awsglue.context import GlueContext
from pyspark.context import SparkContext


# Configurações iniciais do Spark
spark = SparkSession.builder \
    .appName("Carga Dados Origem para RAW") \
    .getOrCreate()

# Configuração dos caminhos S3
bucket_origem = "s3://carteiracotacoes/"
bucket_raw = "s3://hbucket-raw/"

# Leitura dos dados de origem
# Os arquivos CSV são carregados diretamente do bucket de origem
df_clientes = spark.read.csv(f"{bucket_origem}clientes.csv", header=True, sep=";")
df_carteira = spark.read.csv(f"{bucket_origem}carteira.csv", header=True, sep=";")
df_cotacao = spark.read.csv(f"{bucket_origem}cotacao.csv", header=True, sep=",")

# Escrita dos dados na camada RAW
# O formato CSV é mantido para preservar o esquema original dos dados
df_clientes.write.csv(f"{bucket_raw}clientes", mode="overwrite", header=True)
df_carteira.write.csv(f"{bucket_raw}carteira", mode="overwrite", header=True)
df_cotacao.write.csv(f"{bucket_raw}cotacao", mode="overwrite", header=True)

# Logging
print("Dados carregados da origem para a camada RAW com sucesso.")
