# Trabalho de Word Count com Hadoop e Spark (PySpark)

## Ferramentas
- Java 11 (https://www.oracle.com/br/java/technologies/javase/jdk11-archive-downloads.html)
- Hadoop (https://www.apache.org/dyn/closer.cgi/hadoop/common/hadoop-3.4.1/hadoop-3.4.1.tar.gz)
- Spark (https://www.apache.org/dyn/closer.lua/spark/spark-3.5.5/spark-3.5.5-bin-hadoop3.tgz)
- Python 3.11.0 (https://www.python.org/downloads/release/python-3110/)
- Winutils (https://github.com/steveloughran/winutils/tree/master/hadoop-3.0.0/bin)

## Configurações
- Instale o jave e configure o JAVA_HOME na variável de ambiente
```cmd
set JAVA_HOME="C:\Program Files\Java\jdk-11"
```

- Agora adicione o JAVA_HOME\bin no path
```cmd
set PATH=%PATH%;%JAVA_HOME%\bin
```

- Extraia o Hadoop e depois adiciona a variável de ambiente 'HADOOP_HOME' apontando para a pasta que você extraiu
```cmd
set HADOOP_HOME=F:\Dev\Others\hadoop-3.4.1
```

- Agora adicione o HADOOP_HOME\bin no path
```cmd
set PATH=%PATH%;%HADOOP_HOME%\bin
```

- Extraia o Spark e depois adiciona a variável de ambiente 'SPARK_HOME' apontando para a pasta que você extraiu
```cmd
set SPARK_HOME=F:\Dev\Others\spark-3.5.5-bin-hadoop3
```

- Agora adicione o SPARK_HOME\bin no path
```cmd
set PATH=%PATH%;%SPARK_HOME%\bin
```

- Verifique se o hadoop está funcionando digitando o seguinte comando no terminal
```cmd
hadoop version
```

- Caso dê erro, em relação ao Java, ele pode está dando erro por causa de espaços em branco na variável de ambiente, então altere manualmente,
vá na no HADOOP_HOME\etc\hadoop-env.cmd e edite a seguinte linha, colocando aspas entre o valor da variável
```
set JAVA_HOME="C:\Program Files\Java\jdk-11"
```

- Baixe o winutils compatível com o hadoop (provavelmente o winutils3) e extraia o conteúdo dele dentro do HADOOP_HOME\bin.

- Depois vai no diretório C:\, e crie a hierarquia de pasta 'tmp\hive', caso queira via cmd, está logo abaixo
```cmd
mkdir C:\tmp\hive
```

- Vá onde está instalado o HADOOP, entre na pasta e bin e digite no terminal o seguinte comando, para dar permissões
```cmd
winutils.exe chmod -R 777 C:\tmp\hive
```

- Para o executar o PySpark:
```cmd
spark-submit main.py
```