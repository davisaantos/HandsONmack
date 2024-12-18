import boto3
from pyspark.sql import functions as F
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

# Configuração inicial do Spark
spark = SparkSession.builder \
    .appName("Transformação de SILVER para GOLD") \
    .getOrCreate()

# buckets S3
bucket_silver = "s3://hbucket-silver/"
bucket_gold = "s3://hbucket-gold/"

# DF_SILVER
df_clientes_carteira = spark.read.parquet(f"{bucket_silver}clientes_carteira/")

# Refinamento e validação de dados
# Check de outliers e registros inválidos
df_refinado = df_clientes_carteira.filter(
    (F.col("TotalAtivos") >= 0) & (F.col("SaldoCarteira") >= 0)
)

# Agregação
# Regra de negócio: análise detalhada por cliente
df_gold = df_refinado.groupBy("NomeCliente").agg(
    F.sum("TotalAtivos").alias("TotalAtivosCliente"),
    F.sum("SaldoCarteira").alias("TotalSaldoCarteira"),
    F.avg("PatrimonioTotal").alias("MediaPatrimonioCliente")
).withColumn(
    "TotalGeralPatrimonio",
    F.col("TotalAtivosCliente") + F.col("TotalSaldoCarteira")
)

# Metadados
df_gold = df_gold.withColumn(
    "DataProcessamento",
    F.current_timestamp()
).withColumn(
    "AnoProcessamento",
    F.year(F.col("DataProcessamento"))
).withColumn(
    "MesProcessamento",
    F.month(F.col("DataProcessamento"))
)


# Dados particionados para Athena
df_gold.write.parquet(
    f"{bucket_gold}clientes_analytics",
    mode="overwrite",
    partitionBy=["AnoProcessamento", "MesProcessamento"]
)

# Logging
print("Transformação para a camada GOLD concluída com sucesso.")
