from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('submit', views.submit),
    path('deleteNinja/<str:fName>/<str:lName>', views.delete_ninja),
    path('deleteDojo/<str:dName>', views.delete_dojo),
]


# ====================PROVIDED SOLUTION====================
# urlpatterns = [
#     path('', views.index),
#     path('ninjas/create', views.create_ninja),
#     path('dojos/create', views.create_dojo),
# ]


