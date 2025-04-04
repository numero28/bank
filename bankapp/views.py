from django.shortcuts import render
from .models import Customer, Account
#from .forms import CustomerForm, AccountForm

# Create your views here.
def index(request):
    """The home page for BanK app"""
    return render(request, 'bankapp/index.html')

def customers(request):
    customers = Customer.objects.all()
    context = {
        'customers' : customers
        }
    return render(request, 'bankapp/customers.html', context)

def accounts(request, customer_id):
    customer = Customer.objects.get(id=customer_id)
    accounts = customer.account_set.all()
    context = {        
        'customer': customer,
        'accounts': accounts
        }
    return render(request, 'bankapp/accounts.html', context)
"""
def new_customer(request):
    if request.method != 'POST':
        form = CustomerForm()
    else:
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    
    return render(request, 'bankapp/new_customer.html', context)

def new_account(request):
    if request.method != 'POST':
        form = AccountForm()
    else:
        form = CustomerForm(data=request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form': form}
    
    return render(request, 'bankapp/new_account.html', context)
    """