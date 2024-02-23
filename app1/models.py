# models.py
from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class Review(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    comment = models.TextField()


class Author(models.Model):
    name = models.CharField(max_length=100)
    total_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.name

    def update_total_rating(self):
        ratings = Review.objects.filter(author=self).aggregate(avg_rating=Avg('rating'))['avg_rating'] or 0
        self.total_rating = ratings
        self.save()

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.author.update_total_rating()
