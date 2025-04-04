from django.contrib import admin

from .models import Customer, Account
# Register your models here.
admin.site.register(Customer)
admin.site.register(Account)