from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('maps', views.maps),
    path('index', views.index),
    path('myoffice', views.my_ofice),
]
