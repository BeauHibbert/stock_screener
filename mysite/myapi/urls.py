from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('get-aggs/', views.get_aggs, name='get_aggs'),
]