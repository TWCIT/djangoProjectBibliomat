from django.test import TestCase
from django.test import TestCase
from .models import Customer, Copy, Title, Loan


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
    def test_customer_str2(self):
        customer = Customer.objects.create(
            first_name='Wiktor',
            last_name='Wołoszyn',
            email='lubiesok@gmail.com',
            phone_number='669-588-247',
            loan_limit=3
        )
        self.assertEqual(customer.first_name, 'Wiktor')
        self.assertEqual(customer.last_name, 'Wołoszyn')
        self.assertEqual(customer.email, 'lubiesok@gmail.com')
        self.assertEqual(customer.phone_number, '669-588-247')
        self.assertEqual(customer.loan_limit, 3)

    def test_customer_str3(self):
        customer = Customer.objects.create(
            first_name='Marek',
            last_name='Wala',
            email='lubieciastka@gmail.com',
            phone_number='669-885-742',
            loan_limit=3
        )
        self.assertEqual(customer.first_name, 'Marek')
        self.assertEqual(customer.last_name, 'Wala')
        self.assertEqual(customer.email, 'lubieciastka@gmail.com')
        self.assertEqual(customer.phone_number, '669-885-742')
        self.assertEqual(customer.loan_limit, 3)

    def test_customer_str4(self):
        customer = Customer.objects.create(
            first_name='Michał',
            last_name='Wolniak',
            email='lubiepomarancze@gmail.com',
            phone_number='966-858-477',
            loan_limit=3
        )
        self.assertEqual(customer.first_name, 'Michał')
        self.assertEqual(customer.last_name, 'Wolniak')
        self.assertEqual(customer.email, 'lubiepomarancze@gmail.com')
        self.assertEqual(customer.phone_number, '966-858-477')
        self.assertEqual(customer.loan_limit, 77777777777007777777777)

    def test_copy_creation(self):
        copy = Copy.objects.create(
            signature='Stephen King',
            is_available=True,
            is_in_bibliomat=True,
            title='The Outsider',
        )
        self.assertEqual(copy.signature, 'Stephen King')
        self.assertEqual(copy.is_available, True)
        self.assertEqual(copy.is_in_bibliomat, True)
        self.assertEqual(copy.title, 'The Outsider')

    def test_title_creation(self):
        title = Title.objects.create(
            title='The Outsider',
            author='Stephen King',
            description='Bestialska zbrodnia. Śledztwo pełne znaków zapytania. Stephen King, znajdujący się w...',
            max_loan_period='62',
        )
        self.assertEqual(title.title, 'The Outsider')
        self.assertEqual(title.author, 'Stephen King')
        self.assertEqual(title.description, 'Bestialska zbrodnia. Śledztwo pełne znaków zapytania. Stephen King, '
                                            'znajdujący się w...')
        self.assertEqual(title.max_loan_period, '62')

    def test_loan_creation(self):
        loan = Loan.objects.create(
            copy='2578',
            customer='Tomek Gondek',
            loan_date='25.02.2023',
            return_date='25.03.2023',
            is_delayed='0',
        )
        self.assertEqual(loan.copy, '2578')
        self.assertEqual(loan.customer, 'Tomek Gondek')
        self.assertEqual(loan.loan_date, '25.02.2023')
        self.assertEqual(loan.return_date, '25.03.2023')
        self.assertEqual(loan.is_delayed, '0')
