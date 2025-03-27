import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

from pyspark import SparkConf
from pyspark.sql import SparkSession
from pyspark.sql.functions import explode, split, col

# gera uma configuração maior pois o mapReduce usa mais ram
conf = SparkConf().setAppName("WordCountApp") \
    .set("spark.executor.memory", "2g") \
    .set("spark.driver.memory", "2g") \
    .set("spark.executor.cores", "2") \
    .set("spark.driver.cores", "2") \
    .set("spark.hadoop.fs.file.impl", "org.apache.hadoop.fs.LocalFileSystem")

spark = SparkSession.builder.config(conf=conf).getOrCreate()

input_path = "entrada.txt" 

text_df = spark.read.text(input_path)

# é muito parecido com o do main.py, as diferenças:
# 1) logo após o explode, ele faz rdd.map passando uma função lambda como parâmetro, que retorna uma tupla, ai ele pega o index 0 (palavra) e o index 1 (contador da palavra)
# 2) já na próxima linha, ele faz o reduce, passando uma função lambda que recebe 2 tuplas, ai ele soma as 2 tuplas, na qual o apache irá somar quando tiver palavras iguais, soma o contador
# 3) gera o dataframe do spark com as colunas word e count
# 4) faz a ordenação padrão, pela coluna de count descendente
word_counts = text_df.select(explode(split(col("value"), "\\s+")).alias("word")) \
    .rdd.map(lambda row: (row[0], 1)) \
    .reduceByKey(lambda a, b: a + b, numPartitions=10) \
    .toDF(["word", "count"]) \
    .orderBy(col("count").desc())

output_path = "saida_mapReduce.csv"

word_counts.write.csv(output_path, header=True, mode="overwrite")

spark.stop()