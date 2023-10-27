from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index),
    path('profile/', views.profile),
    path('maps', views.maps),
    path('index', views.index),
    path('myoffice', views.my_ofice),
    path('toggle_lamp/', views.toggle_lamp, name='toggle_lamp'),
]
