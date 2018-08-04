import os
import sys
import django
import io

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myTunes.settings")
from django.core.management import execute_from_command_line

#sys.path.append(os.path.join(BASE_DIR, 'myTunes'))
sys.path.append("C:\\mystuff\\UWCS564\\project\\sharedFiles\\MusicApp\\myTunes")

django.setup()

from tunesApp.models import Genre, Album, Artist, Song
from tunesApp.models import Song_Likes, Genre_Likes, Artist_Likes
from django.contrib.auth.models import User


newline = '\n'
delim = ','
data_dir = os.getcwd() + '\\raw-files\\'

def load_artists(filename='artist_nodup_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as artist_file:
		for line in artist_file:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			artist = Artist(artist_id=attr_list[0], artist_name=attr_list[1])
			artist.save()
	print("Artists file loaded!!")


def load_albums(filename='album_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as album_file:
		for line in album_file:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			album = Album(album_id=attr_list[0],album_name=attr_list[1])
			album.save()
	print("Albums file loaded!!")

def load_genres(filename='genre_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as genre_file:
		for line in genre_file:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			genre = Genre(genre_id=int(attr_list[0]), label=attr_list[1])
			genre.save()
	print("Genre file loaded!!")

def load_songs(filename='song_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as sg_file:
		for line in sg_file:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			try:
				sg = Song(song_id=attr_list[0],title=attr_list[1],song_key=attr_list[2],time_signature=attr_list[3],
					duration=attr_list[4],energy=attr_list[5],tempo=attr_list[6],loudness=attr_list[7],year=attr_list[8],
					danceability=attr_list[9],writer=attr_list[10],artist_hottness=attr_list[11])
				sg.save()
			except:
				continue
	print("Songs file loaded!!")


def load_plays(filename='plays_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as sg_art_file:
		for line in sg_art_file:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			try:
				one_sg = Song.objects.get(pk=attr_list[0])
				one_art = Artist.objects.get(pk=attr_list[1])
				one_sg.song_artists.add(one_art)
				one_sg.save()
			except:
				continue
	print("Song and artists file loaded!!")

def load_appears(filename='appearsin_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as sg_alb_file:
		for line in sg_alb_file:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			try:
				one_sg = Song.objects.get(pk=attr_list[0])
				one_alb = Album.objects.get(pk=int(attr_list[1]))
				one_sg.song_albums.add(one_alb)
				one_sg.save()
			except:
				continue
	print("Song and albums file loaded!!")


def load_sg_genres(filename='belongs_to_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as sg_genre_file:
		for line in sg_genre_file:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			try:
				one_sg = Song.objects.get(pk=attr_list[0])
				one_genre = Genre.objects.get(pk=attr_list[1])
				one_sg.song_genres.add(one_genre)
				one_sg.save()
			except:
				continue
	print("Song and genre file loaded!!")

def load_user(filename='user_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as user_file:
		for line in user_file:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			try:
				u_name = attr_list[0]
				u_email = attr_list[1]
				one_user = User.objects.create_user(u_name, u_email, password='dbadmin123')
				one_user.first_name = attr_list[2]
				one_user.last_name = attr_list[3]
				one_user.save()
			except:
				continue
	print("Users file loaded!!")


def load_user_likes_song(filename='song_likes_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as user_likes_sg:
		for line in user_likes_sg:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			try:
				sg = Song.objects.get(pk=attr_list[0])
				one_user = User.objects.get(username=attr_list[1])
				sg_likes = Song_Likes(song_id=sg,user_id=one_user,count=attr_list[2],rating=attr_list[3])
				sg_likes.save()
			except:
				continue
	print("Song likes loaded!!")


def load_user_likes_genre(filename='genre_likes_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as user_likes_genre:
		for line in user_likes_genre:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			try:
				genre = Genre.objects.get(pk=int(attr_list[0]))
				one_user = User.objects.get(username=attr_list[1])
				one_genre_likes = Genre_Likes(genre_id=genre,user_id=one_user,rating=attr_list[2])
				one_genre_likes.save()
			except:
				continue
	print("User genre likes loaded!!")


def load_user_likes_artists(filename='artist_likes_v1.csv'):
	with open(data_dir + filename,'r',encoding="utf8") as user_likes_artist:
		for line in user_likes_artist:
			line = line.rstrip(newline)
			attr_list = line.split(delim)
			try:
				one_artist = Artist.objects.get(pk=attr_list[0])
				one_user = User.objects.get(username=attr_list[1])
				one_artist_likes = Artist_Likes(artist_id=one_artist,user_id=one_user,rating=attr_list[2])
				one_artist_likes.save()
			except:
				continue
	print("User artist likes loaded!!")

def remove_duplicates(input_filename, output_filename):
	lines_seen = set()
	out_file = io.open(output_filename,'w+',encoding="utf8")
	with open(input_filename,'r',encoding="utf8") as in_file:
		for line in in_file:
			if line not in lines_seen:
				out_file.write(line)
				lines_seen.add(line)
	out_file.close()

