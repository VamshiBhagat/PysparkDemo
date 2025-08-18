from pyspark.sql import SparkSession

# Initialize Spark session
spark = SparkSession.builder.appName("SparkSubmitExample").getOrCreate()

# Sample DataFrame
data = [("Alice", 28), ("Bob", 35), ("Cathy", 23)]
columns = ["name", "age"]

df = spark.createDataFrame(data, columns)

# Show DataFrame
df.show()

# Stop session
spark.stop()
