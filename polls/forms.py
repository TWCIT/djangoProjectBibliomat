from django import forms
from .models import Customer

class OrderForm(forms.Form):
    #customer = forms.ModelChoiceField(queryset=Customer.objects.all())
    pick_up_in_bibliomat = forms.BooleanField(required=False)