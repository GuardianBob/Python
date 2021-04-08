from .models import Book, Author
from loginApp.models import User
from django import forms
import datetime

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        self.fields['desc'].label = "Description"
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['desc'].widget.attrs.update({ 'rows': '4' })

    class Meta:
        model = Book
        fields = ['title', 'desc']

    def clean(self):
        super(BookForm, self).clean()
        title = self.cleaned_data.get('title')
        desc = self.cleaned_data.get('desc')
        if len(title) < 2:
            self.errors['title'] = self.error_class([
                'A minimum of 2 characters is required'])
        if len(desc) < 10:
            self.errors['desc'] = self.error_class([
                'A minimum of 10 characters is required'])
        return self.cleaned_data
        