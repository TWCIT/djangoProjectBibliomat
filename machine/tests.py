from django.test import TestCase
from django.contrib.auth.models import User
from .models import Deposit
from polls.models import Customer, Title, Copy, Loan


# Create your tests here.
class DepositTests(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user('testuser', password='pass')
        self.customer = Customer.objects.create(user=self.user)
        self.title = Title.objects.create(name='test', description='test', max_loan_period=2, author='test')
        self.copy = Copy.objects.create(title=self.title, signature='a', is_available=True, is_in_bibliomat=True)
        self.loan = Loan.objects.create(copy=self.copy, customer=self.customer)

    def test_right_user(self):
        deposit = Deposit.objects.create(loan=self.loan, tray=166)

        self.assertEqual(deposit.loan.customer.user, self.user)

        deposit.delete()

        self.assertIsNone(deposit)

