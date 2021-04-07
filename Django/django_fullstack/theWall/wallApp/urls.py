from django.urls import path
from . import views

urlpatterns = [
    path('wall', views.index),
    path('post/<str:content>', views.post),
    path('delete/<str:content>/<int:user_id>/<int:msg_id>', views.delete_msg),
    ]