from django.utils import timezone
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
    rental_date = models.DateTimeField()
    return_date = models.DateTimeField(null=True, blank=True)
    returned = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.id:  # Nuevo objeto
            self.rental_date = timezone.now()  # Establecer la fecha de alquiler al crear
        super(Rental, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer_name} - {self.costume.name}"

