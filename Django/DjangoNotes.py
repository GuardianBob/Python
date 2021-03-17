# There are occasions where the data passed through the url is handled as a parameter. 
# When passing a parameter through the url, you must be explicit of type.
# Here are a few examples, to demonstrate the syntax:

# some_project/some_app/urls.py
urlpatterns = [
    path('bears', views.one_method),                        # would only match localhost:8000/bears
    path('bears/<int:my_val>', views.another_method),       # would match localhost:8000/bears/23
    path('bears/<str:name>/poke', views.yet_another),       # would match localhost:8000/bears/pooh/poke
    path('<int:id>/<str:color>', views.one_more),           # would match localhost:8000/17/brown
]

# If we are passing dynamic data through the url via a GET request, 
# we need to write our corresponding functions to expect this data. 
# The corresponding functions would then look like this:

# some_project/some_app/views.py
def one_method(request):                # no values passed via URL
    pass
    
def another_method(request, my_val):	# my_val would be a number from the URL
    pass                                # given the example above, my_val would be 23
    
def yet_another(request, name):         # name would be a string from the URL
    pass                                # given the example above, name would be 'pooh'
    
def one_more(request, id, color): 	    # id would be a number, and color a string from the URL
    pass                                # given the example above, id would be 17 and color would be 'brown'