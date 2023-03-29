from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    loan_limit = models.PositiveIntegerField()
    user = models.OneToOneField(User, models.CASCADE, related_name='customer')

class Title(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    description = models.TextField()
    max_loan_period = models.PositiveIntegerField()
class Copy(models.Model):
    signature = models.CharField(max_length=50)
    is_available = models.BooleanField()
    is_in_bibliomat = models.BooleanField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE)
class Loan(models.Model):
    copy = models.ForeignKey(Copy, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    loan_date = models.DateField(null=True)
    return_date = models.DateField(null=True)
    is_delayed = models.BooleanField(default=False)