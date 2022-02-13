from django import forms
from .models import BusDetails,Ticket

class Ticket(forms.ModelForm):
    class Meta:
        model=Ticket
        fields="__all__"