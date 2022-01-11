from django.contrib import admin
from .models import  Superuser, Employee
# Register your models here.

# admin.site.register(User)
admin.site.register(Superuser)
admin.site.register(Employee)
