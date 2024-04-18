from django.contrib import admin
from .models import me, Payment, Usermoney
# Register your models here.

admin.site.register(me)
admin.site.register(Payment)
admin.site.register(Usermoney)

