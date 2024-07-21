from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.URLField()
    rating = models.IntegerField(default=0)
    genres = models.ManyToManyField(Genre, related_name='movies')  # Relación de muchos a muchos con Genre
    in_theaters = models.BooleanField(default=False)

    def __str__(self):
        return self.name

