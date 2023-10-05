dim_df = spark.read.format("csv").load("/FileStore/tables/DIM_ACCOUNT.csv",inferSchema=True,header=True)
display(dim_df)
