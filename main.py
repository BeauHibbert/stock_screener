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


