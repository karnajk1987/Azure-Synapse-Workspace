import pyspark.sql.functions as f
sql_df = sqlContext.createDataFrame([('Reshwanth',9,'Bangalore'),('Vikranth',5,'Bangalore')],['name','age','Location'])
display(sql_df)
