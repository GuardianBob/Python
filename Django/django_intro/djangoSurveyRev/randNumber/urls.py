from django.urls import path
from . import views

urlpatterns = [
    path('random_word', views.index),
    path('generate', views.get),
    path('random_word/reset', views.reset),
    ]