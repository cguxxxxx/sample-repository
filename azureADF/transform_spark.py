import sys
from operator import add

from pyspark.sql import SparkSession

def main():
    spark = SparkSession\
        .builder\
        .appName("PythonWordCount")\
        .getOrCreate()

    lines = spark.read.text("wasbs://adftutorial@adftrialch.blob.core.windows.net/spark/inputfiles/minecraftstory.txt").rdd.map(lambda r: r[0])
    counts = lines.flatMap(lambda x: x.split(' ')) \
        .map(lambda x: (x, 1)) \
        .reduceByKey(add)
    counts.saveAsTextFile("wasbs://adftutorial@adftrialch.blob.core.windows.net/spark/outputfiles/wordcount")

    spark.stop()

if __name__ == "__main__":
    main()