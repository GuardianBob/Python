from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('reset', views.reset),
    path('<str:loc>/<int:highV>/<int:lowV>', views.process_money),
    ]