from django import forms
from .models import Book


# creating a form

class Book_form(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"
        
