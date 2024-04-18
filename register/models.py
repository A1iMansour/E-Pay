from django.db import models
import datetime


class me(models.Model):
    job= models.CharField(max_length=100)
    address= models.CharField(max_length=200)
    
    def __str__(self) :
        return self.job
    
CURRENCY=(
    ('G', 'GB Pounds'),
    ('U', 'US Dollars'),
    ('E', 'Euros'),
)

class Usermoney(models.Model):
    currency = models.CharField(max_length=1, choices=CURRENCY)

    def __str__(self):
       return self.currency

class Payment(models.Model):
    userfrom= models.CharField(max_length=100)
    userto= models.CharField(max_length=100)
    done = models.BooleanField( default=False) # if payment is successful=> true
    payment= models.DecimalField(default= 0, decimal_places=4, max_digits=11)
    currency = models.CharField(max_length=1, choices=CURRENCY)
    dat= models.DateField(default=datetime.datetime.today)  
    def __str__(self):
       return f'{self.userfrom} {self.userto}'