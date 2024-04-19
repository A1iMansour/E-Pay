from django.db import models
from django.contrib.auth.models import User
import datetime
CURRENCY=(
    ('G', 'GB Pounds'),
    ('U', 'US Dollars'),
    ('E', 'Euros'),
)
# Create your models here.
class Payment(models.Model):
    userfrom= models.CharField(max_length=100)
    userto= models.CharField(max_length=100)
    payment= models.DecimalField(default= 0, decimal_places=4, max_digits=11)
    currency = models.CharField(max_length=1, choices=CURRENCY)
    dat= models.DateField(default=datetime.datetime.today)  
    def __str__(self):
       return f'from {self.userfrom} to {self.userto}'
    
class Request(models.Model):
    userfrom= models.CharField(max_length=100)
    userto= models.CharField(max_length=100)
    payment= models.DecimalField(default= 0, decimal_places=4, max_digits=11)
    currency = models.CharField(max_length=1, choices=CURRENCY)
    dat= models.DateField(default=datetime.datetime.today)  
    def __str__(self):
       return f'from {self.userfrom} to {self.userto}'
    
class Notify(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message