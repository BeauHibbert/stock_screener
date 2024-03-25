import requests
from polygon import RESTClient
from polygon.rest import models


response = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=Aiz3ZL5A4jU2NbBt2G0bmyD35id5PWZ8") 

print(response.status_code)




client = RESTClient(api_key="Aiz3ZL5A4jU2NbBt2G0bmyD35id5PWZ8")

aggs = client.get_aggs(
    "AAPL",
    1,
    "day",
    "2022-04-04",
    "2022-04-04",
)
print(aggs)



# ticker = "AAPL"

# # List Aggregates (Bars)
# aggs = []
# for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
#     aggs.append(a)

# print(aggs)

# # Get Last Trade
# trade = client.get_last_trade(ticker=ticker)
# print(trade)

# # List Trades
# trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
# for trade in trades:
#     print(trade)

# # Get Last Quote
# quote = client.get_last_quote(ticker=ticker)
# print(quote)

# # List Quotes
# quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
# for quote in quotes:
#     print(quote)