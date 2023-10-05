dim_df.write.format("delta").mode("append").saveAsTable("sample.emp")
