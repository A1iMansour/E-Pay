# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class SignUpForm(UserCreationForm):
    currency_choices = (
        ('GBP', 'GBP'),
        ('USD', 'USD'),
        ('EUR', 'EUR')
        # Add more currency options as needed
    )
    currency = forms.ChoiceField(choices=currency_choices)
    email = forms.EmailField()
   
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email', 'password1', 'password2']

class AdminRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    currency_choices = (
        ('GBP', 'GBP'),
        ('USD', 'USD'),
        ('EUR', 'EUR')
        # Add more currency options as needed
    )
    currency = forms.ChoiceField(choices=currency_choices)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']