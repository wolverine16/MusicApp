from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# TODO(Luis): I arbitrarily picked 150 as the max_length for text field--we should consider if we need a different value. Also, maybe we should make it a global variable instead?

class Genre(models.Model):
    label = models.CharField('label', max_length = 20)
    genre_id = models.IntegerField(primary_key = True)
    
    
class Artist(models.Model):
    artist_id = models.CharField('artist_id', max_length = 30, primary_key = True)
    artist_name = models.CharField(max_length = 150)
    
    
class Album(models.Model):
    album_id = models.IntegerField(primary_key = True)
    album_name = models.CharField(max_length = 150)
    

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
    artist_hottness = models.FloatField()
    song_genres = models.ManyToManyField(Genre)
    song_albums = models.ManyToManyField(Album)
    song_artists = models.ManyToManyField(Artist)
    

class Search(models.Model):
    # TODO: user_id should be AutoField on User model
    # Note: A database index is automatically created on the ForeignKey. You can disable this by setting db_index to False.
    # Note: "_id" is automatically appended to the column name
    # user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    # search_inst will automatically be created with current time/date
    # Note: This should be set to unique=True, but we can't do that without having a composite key. See note below
    # TODO: Django does not appear to support composite keys... need to think of a workaround
    search_id = models.AutoField(primary_key = True) #auto-incremented id, so composite keys not needed
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    album = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    song = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    search_attr = models.CharField(max_length=750)
    search_inst = models.DateTimeField(default=timezone.now)


class Song_Likes(models.Model):
    like_id = models.AutoField(primary_key = True)
    song_id = models.ManyToManyField(Song)
    user_id = models.ManyToManyField(User)
    count = models.IntegerField()
    rating = models.IntegerField() 

class Genre_Likes(models.Model):
    like_id = models.AutoField(primary_key = True)
    genre_id = models.ManyToManyField(Genre)
    user_id = models.ManyToManyField(User)
    rating = models.IntegerField() 

class Artist_Likes(models.Model):
    like_id = models.AutoField(primary_key = True)
    artist_id = models.ManyToManyField(Artist)
    user_id = models.ManyToManyField(User)
    rating = models.IntegerField()


