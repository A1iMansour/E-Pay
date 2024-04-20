from django.db import models
from django.contrib.auth.models import User


class me(models.Model):
    job= models.CharField(max_length=100)
    address= models.CharField(max_length=200)
    
    def __str__(self) :
        return self.job
    
CURRENCY=(
    ('GBP', 'GBP'),
    ('USD', 'USD'),
    ('EUR', 'EUR')
)
class Usermoney(models.Model):
    user=  models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_money', default=None)
    currency = models.CharField(max_length=10, choices=CURRENCY)
    balance = models.DecimalField(default= 100, decimal_places=4, max_digits=11)
    def __str__(self):
       return f'{self.currency} {self.balance}'

