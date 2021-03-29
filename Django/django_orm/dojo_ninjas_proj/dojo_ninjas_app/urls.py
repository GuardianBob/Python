from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit', views.submit),
    path('deleteNinja/<str:fName>/<str:lName>', views.delete_ninja),
    path('deleteDojo/<str:dName>', views.delete_dojo),
]



