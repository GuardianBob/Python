from django.urls import path        # These are the standard imports
from . import views

urlpatterns = [    
    path('admin', views.admin),
    path('dashboard', views.dashboard),
    path('users/new', views.new_user),
    path('users/edit', views.edit_profile),
    path('users/show/<int:user_id>', views.show_user),
    path('users/edit/<int:user_id>', views.edit_user),
    path('users/remove/<int:user_id>', views.remove_user),
    path('update_password', views.update_password),
    path('update_user', views.update_user),
]