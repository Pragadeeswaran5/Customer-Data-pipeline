from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder     .appName("CustomerPurchaseETL")     .getOrCreate()

# Load data from GCS
input_path = "gs://customer-data-bucket/raw/customer_purchases.csv"
raw_data = spark.read.csv(input_path, header=True, inferSchema=True)

# Transform data (Example: Add a calculated column for total purchase amount)
transformed_data = raw_data.withColumn(
    "total_purchase_amount", col("quantity") * col("price_per_unit")
)

# Save transformed data back to GCS
output_path = "gs://customer-data-bucket/processed/customer_purchases_transformed.parquet"
transformed_data.write.parquet(output_path, mode="overwrite")

spark.stop()