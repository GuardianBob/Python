from django.shortcuts import render, redirect
from .models import User
from django.forms.models import model_to_dict

def index(request):
    all_users = User.objects.all()
    # all_fields = User._meta.get_fields()    # Get field names
    # obj2 = all_fields[1].name   #get actual name of field
    # obj1 = all_users[0]         
    # name = getattr(obj1, obj2)      #Gets the value of the second field for the first user
    # print(name, len(all_fields))

    users = {}
    n = 0
    for i in all_users:
        users[str(n)] = {
            'id':all_users[n].id,
            'name':all_users[n].first_name + " " + all_users[n].last_name,
            'email':all_users[n].email_address,
            'age':all_users[n].age
        }
        n +=1
    # print(users)

    # Iterate through nested dictionary
    # for p_k, p_v in users.items():  
    #     for value in p_v:
    #         print(p_v[value])
    context = {
        "all_users": users
    }
    return render(request, 'index.html', context)

def submit(request):
    
    return redirect('/')