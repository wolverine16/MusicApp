from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_label = models.CharField('label', max_length = 20)

class Album(models.Model):
    album_name = models.CharField
