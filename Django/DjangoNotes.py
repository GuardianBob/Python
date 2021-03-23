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

#==============================TEMPLATES=====================================

#For storing your HTML files, Django expects a folder named exactly templates which we will need to create. 
# Each app will have its own templates folder.
# projName > appName > templates

# Assuming we've got the folder structure set up properly, 
# we can then render templates in our views.py folder like so:

# project_name/app_name/views.py
from django.shortcuts import render	# notice the import!
def index(request):
    return render(request, "index.html")

# When we call the render function, our first argument will always be request, 
# and the second argument will be a string indicating which html file to render.

# Passing Data to the Template

# In Django, we are also able to pass data to the template via the render method, 
# but rather than being able to pass up any number of arguments, we can only pass 
# a single dictionary whose keys will be the variable names available on the template. 
# For example:

# project_name/app_name/views.py     
from django.shortcuts import render
    
def index(request):
    context = {
    	"name": "Noelle",
    	"favorite_color": "turquoise",
    	"pets": ["Bruce", "Fitz", "Georgie"]
    }
    return render(request, "index.html", context)

# project_name/app_name/templates/index.html
<h1>Info From Server:</h1>
<p>Name: {{name}}</p>
<p>Color: {{favorite_color}}</p>
<p>Pets</p>
<ul>
{% for pet in pets %}
   <li>{{pet}}</li>
{% endfor %}
</ul>

# Note: You cannot use square brackets with Django's template engine! Instead, use dot notation. 
# For example, array[0] becomes {{ array.0 }}