from django.urls import path
from . import views

urlpatterns = [
    path('hello-world/', views.hello_world, name='hello_world'),
    path('get-open/', views.get_open, name='get_open'),
    path('get-close/', views.get_close, name='get_close')
]
