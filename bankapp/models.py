from django.db import models

# Create your models here.
currency = "GHS"

class Customer(models.Model):
    """Holds records of a customer"""
    cust_id = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
    mname = models.CharField(max_length=200)
    address = models.TextField()
    email = models.EmailField()
    next_of_kin = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.fname} {self.mname} {self.lname}"


class Account(models.Model):
    """Keeps data about an account"""
    holder = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_number = models.IntegerField()
    balance = models.FloatField()     
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.account_number} {currency} {self.balance:,.2f}"
    