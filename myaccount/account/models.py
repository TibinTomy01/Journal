from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    description = models.CharField(max_length=255)
    TRANSACTIONAL_CHOICES=[(1,'Credit'),(0,'Debit')]
    transaction_type =models.IntegerField(choices=TRANSACTIONAL_CHOICES,default=1)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
