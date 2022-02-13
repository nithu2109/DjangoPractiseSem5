from django import forms
from . import models


class emp_form(forms.ModelForm):
    class Meta:
        model = models.emploee_details
        fields = "__all__"
