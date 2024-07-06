from django import forms
from .models import Costume, Rental

class CostumeForm(forms.ModelForm):
    class Meta:
        model = Costume
        fields = ['name', 'description', 'available']

    def clean_name(self):
        name = self.cleaned_data['name']
        # Agregar validaciones adicionales si es necesario
        return name

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['costume', 'customer_name', 'rental_date', 'return_date', 'returned']

    def clean_customer_name(self):
        customer_name = self.cleaned_data['customer_name']
        # Agregar validaciones adicionales si es necesario
        return customer_name

