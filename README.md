# FML
Finance Machine Learning

*"Because everyone else is autistic"*


## DataFetcher
This contains code to retrieve data from various types of backends.

### TD Ameritrade
1. Register at https://developer.tdameritrade.com/ for an API Key
2. Add a **APIKEY.apikey** file to the TDAmeritrade Folder 
3. Copy your API key from step 1 into the first line of this file.
    - **DO NOT COMMIT THIS FILE (.gitignore is set for \*.apikey)**

#### Option Data
#### Equity Data
##### Usage:
Create a new instance of an Equity class by passing the string of the ticker symbol.
```
AMD = Equity("AMD")
AMD.get_price() //returns the current price

```
###  ETF Data

## DataProvider

The DataProvider class is meant to be the main class used to generate training data from data.

```
    dp = DataProvider()
    dp.add_equity(AMD)
    dp.add_equity(INTC)
    dp.set_data_getter(r)
    (data, label) = dp.get_train_data_single(random=True)
    (data, label) = dp.get_train_data_next()


   