from .models import Book, Author, Review
from loginApp.models import User
from django import forms
import datetime

class BookForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap        
        
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })        

        # self.fields['review'] = forms.Textarea()
        # self.fields['author'] = forms.CharField(max_length=45, )
        # self.fields['rating'] = forms.ChoiceField()

        self.fields['desc'].label = "Description"
        self.fields['desc'].widget.attrs.update({ 'rows': '4' })

        # self.fields['review'].label = "Review"        
        # self.fields['review'].widget.attrs.update({ 'rows': '4' })
        
        # self.fields['rating'].label = "Rating"        
        # self.fields['rating'].widget.attrs.update({ 'class':'btn btn-outline-secondary dropdown-toggle form-control mb-4' })
        

    class Meta:
        model = Book
        fields = ('__all__')

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

class ReviewForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })
        self.fields['review'].widget.attrs.update({ 'rows': '4' })

        class Meta:
            model = Review
            fields = ['review', 'rating']

        def clean(self):
            super(BookForm, self).clean()            
            desc = self.cleaned_data.get('desc')            
            if len(desc) < 10:
                self.errors['desc'] = self.error_class([
                    'A minimum of 10 characters is required'])
            return self.cleaned_data

