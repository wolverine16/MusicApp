from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# TODO(Luis): I arbitrarily picked 150 as the max_length for text field--we should consider if we need a different value. Also, maybe we should make it a global variable instead?

class Genre(models.Model):
<<<<<<< HEAD
    label = models.CharField('label', max_length = 30)
=======
    # Attributes of Genre entity
    label = models.CharField('label', max_length = 20)
>>>>>>> 8cafbb4b23c0cd516f8f4b5e020031d40f370116
    genre_id = models.IntegerField(primary_key = True)
    # Relationships connected to Genre entity
    user_genre_likes = models.ManyToManyField(User, through="Genre_Likes")
    
    
class Artist(models.Model):
    # Attributes of Artist entity
    artist_id = models.CharField('artist_id', max_length = 30, primary_key = True)
<<<<<<< HEAD
    artist_name = models.CharField(max_length = 1000)
=======
    artist_name = models.CharField(max_length = 150)
    # Relationships connected to Artist entity
    user_artist_likes = models.ManyToManyField(User, through='Artist_Likes')
>>>>>>> 8cafbb4b23c0cd516f8f4b5e020031d40f370116
    
    
class Album(models.Model):
    #Attributes of Album entity
    album_id = models.IntegerField(primary_key = True)
    album_name = models.CharField(max_length = 1000)
    

class Song(models.Model):
    #Attributes of Song entity
    song_id = models.CharField('song_id', max_length = 30, primary_key = True)
    title = models.CharField('title', max_length = 1000)
    song_key = models.IntegerField()
    time_signature = models.IntegerField()
    duration = models.FloatField()
    energy = models.FloatField()
    tempo = models.FloatField()
    loudness = models.FloatField() 
    year = models.IntegerField()
    danceability = models.FloatField()
    writer = models.CharField('writer', max_length = 1000)
    artist_hottness = models.FloatField()
    #Relationships connected to Song entity
    song_genres = models.ManyToManyField(Genre)
    song_albums = models.ManyToManyField(Album)
    song_artists = models.ManyToManyField(Artist)
    user_song_likes = models.ManyToManyField(User, through='Song_Likes')
    

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
    album = models.CharField(max_length=1000)
    genre = models.CharField(max_length=1000)
    song = models.CharField(max_length=1000)
    artist = models.CharField(max_length=1000)
    search_attr = models.CharField(max_length=1000)
    search_inst = models.DateTimeField(default=timezone.now)

class Song_Likes(models.Model):
    song_id = models.ForeignKey(Song, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    count = models.IntegerField()
    rating = models.IntegerField() 

class Genre_Likes(models.Model):
    genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField() 

class Artist_Likes(models.Model):
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
