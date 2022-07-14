from django.db import models
from django.utils import timezone

# Create your models here.

"""
This is a transaction model:
1. ID, Timestamp, Amount, Phone number, Account number, Transaction status

2. Create view /util to call the Mpesa API (Living under api.pokea.co)

3. Initiate Transaction (C2B via STK push)

4. Listen for Transaction Status updates

"""

class Transactions (models.Model):
    """ Transaction Model"""
    id = models. BigAutoField(primary_key=True, unique=True)
    timestamp = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=30)

    #user = models.ForeignKey(User, on_delete= models.CASCADE)
