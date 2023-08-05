from django import forms
from .models import Message


class MessageForm(forms.ModelForm):
    full_name = forms.CharField(max_length=60, required=True)
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True)
    message = forms.CharField(required=True)    

    class Meta:
        model = Message
        exclude = []