from .models import User
from django import forms
import datetime
import bcrypt

class Register_Form(forms.Form):
    first_name = forms.CharField(max_length=200, widget=forms.TextInput)
    last_name = forms.CharField(max_length=200, widget=forms.TextInput)  
    email = forms.EmailField(max_length=200, widget=forms.EmailInput)
    password = forms.CharField(max_length=20, min_length=8, widget=forms.PasswordInput)
    password_confirm = forms.CharField(max_length=20, min_length=8, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(Register_Form, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class' : 'form-control',
            })

    def clean(self):
        super(Register_Form, self).clean()
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password_confirm = self.cleaned_data.get('password_confirm')
        
        def check_string(string, length):
            if len(string) < length: 
                self.errors[f'{string}'] = self.error_class([
                    f'Input must be at least 2 characters.'])
        
        check_string(first_name, 2)
        check_string(last_name, 2)

        if password != password_confirm:
            self.errors[f'password'] = self.error_class([
                    f'Passwords don\'t match.'])

        return self.cleaned_data

class Login_Form(forms.Form): 
    email = forms.EmailField(max_length=200, widget=forms.EmailInput)
    password = forms.CharField(max_length=20, min_length=8, widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(Login_Form, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class' : 'form-control',
            })

    def clean(self):
        super(Login_Form, self).clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        if not len(User.objects.filter(email=email)) > 0:
            self.errors[f'email'] = self.error_class([
                    f'Email or password is invalid'])
        else:
            stored_data = User.objects.get(email=email)
            if not bcrypt.checkpw(password.encode(), stored_data.password.encode()):
                self.errors[f'email'] = self.error_class([
                    f'Email or password is invalid'])
        return self.cleaned_data