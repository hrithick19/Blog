from django import forms
from .models import contactForm

class Contact_form(forms.ModelForm):
    class Meta:
        model=contactForm
        fields=[
            'name','email','message'
            ]