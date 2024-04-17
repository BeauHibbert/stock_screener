from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('get-from/', views.get_from, name='get_from'),
    path('get-open/', views.get_open, name='get_open'),
    path('get-close/', views.get_close, name='get_close'),
    path('get-high/', views.get_high, name='get_high'),
    path('get-low/', views.get_low, name='get_low')
]
