from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("IntrusionDetection") \
    .master("local[*]") \
    .config("spark.driver.memory","4g") \
    .config("spark.executor.memory","4g") \
    .config("spark.sql.shuffle.partitions","50") \
    .config("spark.memory.fraction","0.6") \
    .config("spark.sql.execution.arrow.pyspark.enabled","true") \
    .getOrCreate()

print("Spark started successfully")
