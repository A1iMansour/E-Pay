# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SignUpForm(UserCreationForm):
    currency_choices = (
        ('G', 'GB Pounds'),
        ('U', 'US Dollars'),
        ('E', 'Euros'),
        # Add more currency options as needed
    )
    currency = forms.ChoiceField(choices=currency_choices)
    email = forms.EmailField()
   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']
