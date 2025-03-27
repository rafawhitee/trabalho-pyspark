import os
import sys

# para funcionar no windows, pois o pyspark tenta usar o python3 ao invés de python
os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# cria o objeto de configuração para o PySpark
conf = SparkConf().setAppName("WordCountApp").set("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem")

# gera de fato o pyspark, a partir da configuração
spark = SparkSession.builder.config(conf=conf).getOrCreate()

# arquivo local, no caso, se fosse o HDFS, seria com o prefixo HDSF://
input_path = "entrada.txt" 

# faz a leitura
text_df = spark.read.text(input_path)

# faz o processamento das linhas/palavras
# select --> função própria do pyspark para 'selecionar' colunas do dataframe que o mesmo gera
# col('value') --> pega somente a coluna value do dataframe do pyspark
# split(col('value'), '\\s+) --> ela separa o valor da coluna value em palavras
# explode --> ela gera uma nova linha para cada item retornado do split
# alias('word') --> a partir do valor retornado do explode, gera uma coluna com o nome chamada 'palavra' que são as palavras
# groupBy('word') --> faz o groupBy baseado na coluna anterior, similar ao de banco de dados, faz o agrupamento pela coluna 'word'
# count --> igual ao de banco de dados e em quase toda linguagem, faz a contagem daquele grupo.
# orderBy(col('count').desc) --> pega a coluna count, que foi criada pelo count, e faz a ordenação de forma descendente (DESC)
word_counts = text_df.select(explode(split(col("value"), "\\s+")).alias("palavra")) \
    .groupBy("palavra") \
    .count() \
    .orderBy(col("count").desc())

# define o nome da saída, no csao em CSV, se fosse o HDFS, seria com o prefixo HDSF://
output_path = "saida.csv"

# a partir do resultado final do processamento anterior, o pyspark já tem uma função que gera em csv
word_counts.write.csv(output_path, header=True, mode="overwrite")

# para o spark
spark.stop()