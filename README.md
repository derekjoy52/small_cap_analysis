# small_cap_analysis
Setting up scalable infrastructure to analyze systematic short edge in the small cap equities market.
Postgres, Spark, Airflow for orchestration and minio as S3 bucket. Slight alterations to from original open sources authors to fix bugs.


Traders have extracted edge pre-2023 era (capacity approx $1M USD/year) from this pattern but the trade has since been crowded. Nowadays, there is significant chance of blow up risk due to liquidity and lock up of float issue if stricter rules aren't applied. However, this lends itself to overfitting issues making this strategy untradableable in it's simpliest form. 

This project is primarily a data engineering portfolio piece and secondarly an analysis of how the Expected Value of this edge has evolved through the years. 

