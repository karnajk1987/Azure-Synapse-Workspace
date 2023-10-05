#Creating Pyspark DataFram using Spark Session...
#my_schema=StructType(List(StructField(name,StringType,true),StructField(age,LongType,true)))
my_df = spark.createDataFrame([('Reshwanth',9),('Vikranth',5)],['name','age'])
type(my_df)  
display(my_df)
