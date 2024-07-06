# rentals/models.py
from django.db import models

class Costume(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Rental(models.Model):
    costume = models.ForeignKey(Costume, on_delete=models.CASCADE)
    customer_name = models.CharField(max_length=100)
    rental_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.customer_name} - {self.costume.name}"

