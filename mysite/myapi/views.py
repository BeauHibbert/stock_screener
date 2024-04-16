from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from polygon import RESTClient
from polygon.rest import models
import requests
from django.http import HttpResponse
from django.http import JsonResponse



@api_view(['GET'])
def hello_world(request):
    return Response({'message': 'Hello, world!'})

# @api_view(['GET'])
# def get_aggs(request):
#     # return Response({'data'})
#     response = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2023-01-09/2023-01-09?apiKey=Aiz3ZL5A4jU2NbBt2G0bmyD35id5PWZ8") 

#     return Response(response)

# @api_view(['GET'])
# def get_macd(request):
#     response = requests.get('https://api.polygon.io/v1/indicators/macd/AAPL?timespan=day&adjusted=true&short_window=12&long_window=26&signal_window=9&series_type=close&order=desc&apiKey=Aiz3ZL5A4jU2NbBt2G0bmyD35id5PWZ8')
  
#     return Response(response)





@api_view(['GET'])
def get_onc(request):
    query = request.query_params['symbol']
    query_upper = query.upper()
    response = requests.get(f'https://api.polygon.io/v1/open-close/{query_upper}/2023-01-09?adjusted=true&apiKey=Aiz3ZL5A4jU2NbBt2G0bmyD35id5PWZ8')

    # print(response)

    if response.status_code == 200:
        return Response(response)
    else:
        error_message = f"Error: {response.status_code}"
        return Response({'error': error_message}, status=500)
    




   