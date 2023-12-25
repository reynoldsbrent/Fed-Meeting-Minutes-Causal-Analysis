# Federal Reserve Meeting Minutes Causal Analysis

 This project explores the connection between the sentiment of Federal Reserve Meeting Minutes and the Dow Jones, Nasdaq, and SP500. Sentiment 

 Sentiment analysis of the Federal Reserve Meeting Minutes was done using VADER Sentiment Analysis. A compound score was used for the sentiment score of each meeting minutes statement. A compound score ranges from -1 (most negative) to +1 (most positive). 

 Correlation and causality of the sentiment scores and the Dow Jones, Nasdaq, and SP500 were explored.

## Results

It was found that there was little correlation between the entiment scores of the Federal Reserve Meeting Minutes and the stock market data from the Dow, Nasdaq, and SP500. 

In addiiton, there was no evidence of granger causality between the sentiment scores and the Dow and SP500 since the P scores of the F Test were not below 0.05. However, there was sufficient evidence to suggest that there was granger causality between the sentment scores and the Nasdaq based off of a P value of the F Test being below 0.05. 

Evidence of granger causality between the sentiment scores and the Nasdaq might be explained in that the Nasdaq is generally more sensitive to change and in general more volatile compared to the Dow and SP500. The sentiment of the meeting minutes might have a greater impact on the Nasdaq than the Dow or SP500.

## Setup

1. Clone the new repo to your machine.
1. Create a virtual environment, activate it, and install the required packages.


### Virtual Environment Step-by-Step Instructions

1. After you have cloned the repo to your machine, 
navigate to the project folder in GitBash/Terminal.
1. Create a virtual environment in the project folder. `python3 -m venv venv` or `virtualenv venv`
1. Activate the virtual environment. `source venv/bin/activate` or `venv\Scripts\activate`
1. Install the required packages. `pip install -r requirements.txt`
1. To deactivate the virtual environment type `deactivate`


## Resources

- This project uses Federal Reserve Meeting Minutes from 2018 to 2022 which can be found in the below links.
- https://www.federalreserve.gov/monetarypolicy/fomc_historical_year.htm
- https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm
