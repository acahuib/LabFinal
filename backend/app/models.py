from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    rating = models.IntegerField(default=0)
    genres = models.JSONField()
    in_theaters = models.BooleanField(default=False)

    def __str__(self):
        return self.name

