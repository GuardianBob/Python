from django import forms

class getInfo(forms.Form):
    name = forms.CharField(max_length=200)
    