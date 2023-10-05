from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a Spark session
spark = SparkSession.builder \
    .appName("PySpark Example") \
    .getOrCreate()

# Read data from a CSV file
input_path = "path/to/input.csv"
df = spark.read.option("header", "true").csv(input_path)

# Perform some transformations (e.g., filter and select specific columns)
filtered_df = df.filter(col("age") >= 18).select("name", "age")

# Write the transformed data to another CSV file
output_path = "path/to/output.csv"
filtered_df.write.option("header", "true").csv(output_path)

# Stop the Spark session
spark.stop()
