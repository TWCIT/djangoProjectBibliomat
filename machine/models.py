from django.db import models
from django.utils import timezone
from polls.models import Loan


# Create your models here.
class Deposit(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, unique=True)
    tray = models.PositiveIntegerField(unique=True)
    date_deposited = models.DateTimeField(default=timezone.now)
