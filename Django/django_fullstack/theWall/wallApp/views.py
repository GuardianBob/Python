from django.shortcuts import render, redirect
from .models import Message, Comment
from loginApp.models import User


def index(request):
    user_id = request.session['user_id']
    user = User.objects.get(id=user_id)
    context = {
        'messages': Message.objects.all(),
        'comments': Comment.objects.all(),
        'user': User.objects.get(id=user_id),
        }
    if 'errors' in request.session:
        context.update({'errors': request.session['errors']})
    return render(request, 'wall.html', context)

def post(request, content):
    if request.method == "GET":
        return redirect('/wall')
    post= {}    
    user = User.objects.get(id=request.session['user_id'])
    if content == "message":
        Message.objects.create(message=request.POST['new_message'], user=user)
    if content == "comment":
        message = Message.objects.get(id=request.POST['message_id'])
        Comment.objects.create(comment=request.POST['new_comment'], message=message, user=user)
    return redirect('/wall')

def delete_msg(request, content, user_id, msg_id):    
    errors = {}
    if content == "comment":
        comment = Comment.objects.get(id=msg_id)
        print(comment.user.id, "==", user_id)
        if comment.user.id == user_id:
            comment.delete()
        else:
            errors.append({"del_msg": "Unable to delete message."})
    if content == "message":
        message = Message.objects.get(id=msg_id)
        print(message.user.id, "==", user_id)
        if message.user.id == user_id:
            message.delete()
        else:
            errors.append({"del_cmt": "Unable to delete message."})
    request.session['errors'] = errors
    return redirect('/wall')