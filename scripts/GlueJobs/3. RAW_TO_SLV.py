import boto3
from pyspark.sql import functions as F
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import types as T

# Configuração inicial do Spark
spark = SparkSession.builder \
    .appName("Transformação de RAW para SILVER") \
    .getOrCreate()

# Configuração dos buckets S3
bucket_raw = "s3://hbucket-raw/"
bucket_silver = "s3://hbucket-silver/"

# Função para validar schemas e detectar problemas de qualidade
def validar_e_corrigir_dados(df, schema, colunas_chave):
    # Aplicar o schema
    df = spark.createDataFrame(df.rdd, schema=schema)
    
    # Remover registros duplicados
    df = df.dropDuplicates(colunas_chave)
    
    # Remove valores nulos em colunas obrigatórias
    colunas_obrigatorias = [campo.name for campo in schema.fields if not campo.nullable]
    df = df.dropna(subset=colunas_obrigatorias)
    
    return df

# Leitura dos dados da camada RAW
df_clientes = spark.read.csv(f"{bucket_raw}clientes", header=True, sep=",")
df_carteira = spark.read.csv(f"{bucket_raw}carteira", header=True, sep=",")
df_cotacao = spark.read.csv(f"{bucket_raw}cotacao", header=True, sep=",")

# Definindo schemas esperados
schema_clientes = T.StructType([
    T.StructField("idCliente", T.StringType(), False),
    T.StructField("NomeCliente", T.StringType(), True),
    T.StructField("SaldoCarteira", T.DoubleType(), False)
])

schema_carteira = T.StructType([
    T.StructField("idCliente", T.StringType(), False),
    T.StructField("CodigoAtivo", T.StringType(), False),
    T.StructField("QtdeAtivo", T.IntegerType(), False)
])

schema_cotacao = T.StructType([
    T.StructField("CodigoAtivo", T.StringType(), False),
    T.StructField("ValorFechamento", T.DoubleType(), False)
])

# Validação e correção de dados
df_clientes = validar_e_corrigir_dados(df_clientes, schema_clientes, ["idCliente"])
df_carteira = validar_e_corrigir_dados(df_carteira, schema_carteira, ["idCliente", "CodigoAtivo"])
df_cotacao = validar_e_corrigir_dados(df_cotacao, schema_cotacao, ["CodigoAtivo"])

# Transformações
# Cálculo do valor total por ativo e cliente
df_carteira_cotacao = df_carteira.join(
    df_cotacao,
    on="CodigoAtivo",
    how="inner"
).withColumn(
    "ValorTotalAtivo",
    F.col("QtdeAtivo") * F.col("ValorFechamento")
)

# Consolidação dos dados por cliente
df_resultado = df_carteira_cotacao.join(
    df_clientes,
    on="idCliente",
    how="inner"
).groupBy(
    "idCliente", "NomeCliente"
).agg(
    F.sum("ValorTotalAtivo").alias("TotalAtivos"),
    F.first("SaldoCarteira").alias("SaldoCarteira")
).withColumn(
    "PatrimonioTotal",
    F.col("TotalAtivos") + F.col("SaldoCarteira")
)

# Escrita dos dados na camada SILVER
df_resultado.write.parquet(
    f"{bucket_silver}clientes_carteira",
    mode="overwrite"
)

# Logging
print("Transformação de RAW para SILVER concluída com sucesso.")
