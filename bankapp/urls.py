"""Defines URL patterns for bankapp."""
from django.urls import path
from . import views

app_name = 'bankapp'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    path('customers/', views.customers, name='customers'),
    path('customers/<int:customer_id>/', views.accounts, name='accounts'),
    #path('new_customer/', views.new_customer, name='new_customer'),
    #path('new_account/', views.new_account, name='new_account'),

]