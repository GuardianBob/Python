from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('get', views.get),
    path('reset', views.reset),
]