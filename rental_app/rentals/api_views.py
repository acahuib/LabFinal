# En rentals/api_views.py

from rest_framework import viewsets
from .models import Costume, Rental
from .serializers import CostumeSerializer, RentalSerializer

class CostumeViewSet(viewsets.ModelViewSet):
    queryset = Costume.objects.all()
    serializer_class = CostumeSerializer

class RentalViewSet(viewsets.ModelViewSet):
    queryset = Rental.objects.all()
    serializer_class = RentalSerializer

