"""
from django import forms
from .models import Customer, Account

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['text']
        labels = {'text':''}
    
class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['text']
        labels = {'text':''}
"""