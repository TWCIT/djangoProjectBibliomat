from django.test import TestCase
from django.test import TestCase
from .models import Customer,  Copy, Title


class CustomerModelTests(TestCase):

    def test_customer_creation(self):
        customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            phone_number='555-555-5555',
            loan_limit=3
        )
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.last_name, 'Doe')
        self.assertEqual(customer.email, 'johndoe@example.com')
        self.assertEqual(customer.phone_number, '555-555-5555')
        self.assertEqual(customer.loan_limit, 3)

    def test_customer_str(self):
        customer = Customer.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            phone_number='555-555-5555',
            loan_limit=3
        )
        self.assertEqual(str(customer), 'John Doe')


# Create your tests here.
