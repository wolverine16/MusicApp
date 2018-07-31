from django.db import models
from django.utils.timezone import now

# Create your models here.

# TODO(Luis): I arbitrarily picked 150 as the max_length for text field--we should consider if we need a different value. Also, maybe we should make it a global variable instead?

class Song(models.Model):
    song_id = models.CharField('song_id', max_length = 30, primary_key = True)
    title = models.CharField('title', max_length = 150)
    key = models.IntegerField()
    time_signature = models.IntegerField()
    duration = models.FloatField()
    energy = models.FloatField()
    tempo = models.FloatField()
    loudness = models.FloatField() 
    year = models.IntegerField()
    danceability = models.FloatField()
    writer = models.CharField('writer', max_length = 150)
    song_genres = models.ManyToManyField(Genre)
    
    
class Genre(models.Model):
    label = models.CharField('label', max_length = 20)
    genre_id = models.IntegerField(primary_key = True)
    
class Album(models.Model):
    album_id = models.IntegerField(primary_key = True)
    album_name = models.CharField(max_length = 150)

class User(models.Model):
    pass

class Search(models.Model):
    # TODO: user_id should be AutoField on User model
    # Note: A database index is automatically created on the ForeignKey. You can disable this by setting db_index to False.
    # Note: "_id" is automatically appended to the column name
    # user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    # search_inst will automatically be created with current time/date
    # Note: This should be set to unique=True, but we can't do that without having a composite key. See note below
    # search_inst = models.DateTimeField(default=timezone.now)
    # TODO: Django does not appear to support composite keys... need to think of a workaround
    album = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    song = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    search_attr = models.CharField(max_length=750)

class Artist(models.Model):
    artist_id = models.IntegerField(primary_key = True)
    artist_name = models.CharField(max_length = 150)
    artist_hottness = models.FloatField()




