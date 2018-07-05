from django.db import models
from django.utils.timezone import now

# Create your models here.

# TODO(Luis): I arbitrarily picked 150 as the max_length for text field--we should consider if we need a different value. Also, maybe we should make it a global variable instead?

class Genre(models.Model):
    genre_label = models.CharField('label', max_length = 20)

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=150)

class User(models.Model):
    pass

class Search(models.Model):
    # TODO: user_id should be AutoField on User model
    # Note: A database index is automatically created on the ForeignKey. You can disable this by setting db_index to False.
    # Note: "_id" is automatically appended to the column name
    user = models.ForeignKey(User, on_delete=models.CASCADE, primary_key=True)
    # search_inst will automatically be created with current time/date
    # Note: This should be set to unique=True, but we can't do that without having a composite key. See note below
    search_inst = models.DateTimeField(default=timezone.now)
    # TODO: Django does not appear to support composite keys... need to think of a workaround
    album = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    song = models.CharField(max_length=150)
    artist = models.CharField(max_length=150)
    search_attr = models.CharField(max_length=750)

