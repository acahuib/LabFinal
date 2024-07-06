# backend/rentals/forms.py

from django import forms
from .models import Costume, Rental

class CostumeForm(forms.ModelForm):
    class Meta:
        model = Costume
        fields = '__all__'

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = '__all__'

