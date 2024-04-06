from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    age = models.SmallIntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    author = models.ForeignKey(Author, blank=False, null=True, on_delete=models.SET_NULL)
    genre = models.ForeignKey(Genre, blank=False, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name