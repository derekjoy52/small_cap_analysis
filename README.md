# small_cap_analysis

I know of retail traders have extracted edge pre-2023 era (capacity of strategy approx $1M USD/year) from this pattern but the trade has since been crowded. Nowadays, there is significant chance of blow up risk due to liquidity and lock up of float issue if stricter rules aren't applied. However, this lends itself to overfitting issues making this strategy untradableable in it's simpliest form. Cue this research project. 

This project is primarily a data engineering portfolio piece and secondarly an analysis of how the Expected Value of this edge has evolved through the years. I actually think retail traders are at a disadvantage if they go fully systematic - but this is for another day.

I've set up scalable infrastructure to analyze systematic short edge in the small cap equities market.
Postgres, Spark, Airflow for orchestration and minio as S3 bucket all within docker containers. Slight alterations from original open sources authors have been made to fix bugs and get the setup operational.


Specifically  I want to test shorting at the open and closing the position at the end of the day. For stocks that opened 30% above their previous close price.

Stocks cannot be nano float. This has to be defined. Let's start with sub 2M shares float.
Stocks cannot be greater than 2B in market cap. 
I want data from Jan 2020 to till Dec 2024.
I need to ensure in my sample the stocks that have since delisted appears otherwise the EV will skew.

I need previous close price, open price, high price, low price, close price. 

