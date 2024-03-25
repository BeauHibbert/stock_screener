from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

@api_view(['GET'])
def get_aggs(request):
    return Response({'message': 'hitting get_aggs request'})
# import requests
# from polygon import RESTClient
# from polygon.rest import models


# response = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=Aiz3ZL5A4jU2NbBt2G0bmyD35id5PWZ8") 

# print(response.status_code)




# client = RESTClient(api_key="Aiz3ZL5A4jU2NbBt2G0bmyD35id5PWZ8")

# aggs = client.get_aggs(
#     "AAPL",
#     1,
#     "day",
#     "2022-04-04",
#     "2022-04-04",
# )
# print(aggs)