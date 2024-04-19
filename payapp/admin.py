from django.contrib import admin
from .models import Request,Notify, Payment

# Register your models here.
admin.site.register(Payment)
admin.site.register(Request)
admin.site.register(Notify)