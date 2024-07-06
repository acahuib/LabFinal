# En rentals/serializers.py

from rest_framework import serializers
from .models import Costume, Rental

class CostumeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Costume
        fields = '__all__'

class RentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rental
        fields = '__all__'

