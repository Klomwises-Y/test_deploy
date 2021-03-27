from django import forms
from .models import Contact
### logic in backend

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['subject','name','email','detail']
