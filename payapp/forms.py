# forms.py
from django import forms
from .models import Request, Payment

class RequestForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ['userto', 'payment', 'currency']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['userto', 'payment', 'currency']
