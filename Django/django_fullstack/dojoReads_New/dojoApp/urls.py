from django.urls import path        # These are the standard imports
from . import views

urlpatterns = [
    path('books', views.books),
    path('books/add', views.add),
    path('books/new_book', views.newBook),
    path('update/<int:bid>', views.update, name="update_submit"),
    path('books/<int:bid>', views.book_info, name="book_info"),
    path('users/<int:uid>', views.user_info),    
    path('books/delete/<int:rid>', views.del_review),
    path('cl/<str:page>/<int:bid>', views.clear),
]