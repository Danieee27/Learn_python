from django import forms
from .models import ShippingAddress

class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Full Name'}), max_length = 200, required = True)
    shipping_email = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Email'}), max_length = 200, required = True)
    shipping_address1 = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Address1'}), max_length = 200, required = True)
    shipping_address2 = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Address2'}), max_length = 200, required = False)
    shipping_city = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'City'}), max_length = 200, required = True)
    shipping_state = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'State'}), max_length = 200, required = True)
    shipping_zipcode = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Zip_Code'}), max_length = 200, required = True)
    shipping_country = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Country'}), max_length = 200, required = True)

    class Meta:
        model = ShippingAddress
        fields = ['shipping_full_name', 'shipping_email', 'shipping_address1', 'shipping_address2', 'shipping_city', 'shipping_state', 'shipping_zipcode', 'shipping_country']

        exclude = ['user',]

class PaymentForm(forms.Form):
    card_name = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'Name on Card'}), max_length = 100, required = True)
    card_number = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': '**** **** **** ****'}), max_length = 20, required = True)
    card_cvvnumber = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'CVV'}), max_length = 3, required = True)
    card_expdate = forms.CharField(label = "", widget = forms.TextInput(attrs = {'class': 'form-control', 'placeholder': 'dd/mm/yyyy'}), max_length = 10, required = True)

