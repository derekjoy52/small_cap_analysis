# small_cap_analysis

I know of retail traders have extracted edge pre-2023 era (capacity of strategy seeems to be approx $1M USD/year) from this pattern but the trade has since been crowded. Nowadays, there is significant chance of blow up risk due to liquidity and lock up of float issue I have seen in the market if stricter rules aren't applied. However, this lends itself to overfitting issues making this strategy untradableable in it's simpliest form. Hence, I want to conduct this research project. 

This project is primarily a data engineering portfolio piece and secondarly an analysis of how the Expected Value of this edge has evolved through the years. I actually think retail traders are at a disadvantage if they go fully systematic. Competing on quality of data and infra + strategy extractation and then robust execution is just too much for one person - but this is for another day.

I've set up scalable infrastructure to analyze systematic short edge in the small cap equities market.
Postgres, Spark, Airflow for orchestration and minio as S3 bucket all within docker containers. Slight alterations from original open sources authors have been made to fix bugs and get the setup operational.


Specifically  I want to test shorting at the open and closing the position at the end of the day. Stop order at 50% above open price. Account for fees and slippage. For stocks that opened 30% above their previous close price.

Criteria:
Security Class: Stock Common, Stock ADR
Market Cap < 200M
 2M<float<10M
 ( [daily][0][open][adjusted] - [daily][-1][close][adjusted] ) / [daily][-1][close][adjusted] * 100 >30 (custom criteria which reduce stock universe substantially)

 

I want data from Jan 2020 to till Dec 2024.
Columns needed:

symbol, date, exchange, close price, open price, high price, low price, volume on day. volume in premarket. premarket high.previous day close.float. market cap.
time of high of day, time of low of day,

