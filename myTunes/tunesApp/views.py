from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
from .forms import SearchForm

import datetime
import decimal


# Create your views here.

def home(request):
	"""The home page for the myTunes app."""
	return render(request, 'home.html')
	
def favorites(request):
	"""Favorites landing page."""
	return render(request, 'favorites_general.html')
	
def favSongs(request):
	"""Favorite songs for the user."""
	cursor = connection.cursor()
	#raw sql to be executed:
	loggedInUser = request.user
	query = '''
	SELECT s.song_id, s.title, s.song_key, s.duration, s.energy, 
	s.tempo, s.danceability, s.time_signature, s.year, s.writer, 
	s.loudness, sl.count, sl.rating, sl.id
	FROM auth_user u, tunesapp_song_likes sl, tunesapp_song s
	WHERE u.id = sl.user_id_id and sl.song_id_id = s.song_id and u.username = %s
	ORDER BY sl.rating DESC;
	'''
	cursor.execute(query,[loggedInUser.username])
	transactions = [to_string(x) for x in cursor.fetchall()]
	keys = ['song_id','title','song_key','duration','energy',
	'tempo','danceability','time_signature','year','writer',
	'loudness','count','rating','id']
	# corresponding numeric value for each key to be used to populate dictionary
	countLst = range(len(keys))
	tempDict = {}
	masterList = []
	for tup in transactions:
		for i in countLst:
			tempDict[keys[i]] = tup[i]
		masterList.append(tempDict)
		tempDict = {}
	# print(masterList)
	return render(request, 'favorite_songs.html',{'masterList':masterList})

def to_string(x):
	'''Function for converting data into string form so that it can be rendered properly'''
	a = []
	for y in x:
		print(type(y),y)
		if type(y) is datetime.datetime:
			a.append(str(y))
		elif type(y) is decimal.Decimal:
			a.append(str(y))
		elif type(y) is float:
			a.append(str(y))
		else:
			a.append(y)
	return a
	

def favArtists(request):
	"""Favorite artists for the user."""
	"""Favorite songs for the user."""
	cursor = connection.cursor()
	#raw sql to be executed:
	loggedInUser = request.user
	query = '''
	SELECT a.artist_id, a.artist_name, al.rating,al.id
	FROM auth_user u, tunesapp_Artist_likes al, tunesapp_Artist a
	WHERE u.id = al.user_id_id and al.artist_id_id = a.artist_id and u.username = %s
	ORDER BY al.rating DESC;
	'''
	cursor.execute(query,[loggedInUser.username])
	transactions = [to_string(x) for x in cursor.fetchall()]
	#print(transactions)
	#transactions = [{"id":1},{"id":2}]
	keys = ['artist_id','artist_name','rating','id']
	# corresponding numeric value for each key to be used to populate dictionary
	countLst = range(len(keys))
	tempDict = {}
	masterList = []
	for tup in transactions:
		for i in countLst:
			tempDict[keys[i]] = tup[i]
		masterList.append(tempDict)
		tempDict = {}
	# print(masterList)
	return render(request, 'favorite_artists.html',{'masterList':masterList})
	
def favGenres(request):
	"""Favorite songs for the user."""
	cursor = connection.cursor()
	#raw sql to be executed:
	loggedInUser = request.user
	query = '''
	SELECT g.genre_id, g.label, gl.rating, gl.id
	FROM auth_user u, tunesapp_Genre_likes gl, tunesapp_Genre g
	WHERE u.id = gl.user_id_id and gl.genre_id_id = g.genre_id and u.username = %s
	ORDER BY gl.rating DESC;
	'''
	cursor.execute(query, [loggedInUser.username])
	transactions = [to_string(x) for x in cursor.fetchall()]
	#print(transactions)
	#transactions = [{"id":1},{"id":2}]
	keys = ['genre_id', 'label', 'rating','id']
	# corresponding numeric value for each key to be used to populate dictionary
	countLst = range(len(keys))
	tempDict = {}
	masterList = []
	for tup in transactions:
		for i in countLst:
			tempDict[keys[i]] = tup[i]
		masterList.append(tempDict)
		tempDict = {}
	return render(request, 'favorite_genres.html',{'masterList':masterList})

def get_search_query(s):
	query_str = '''
	SELECT s.song_id, s.title, s.song_key, s.duration, s.energy, s.tempo, 
	s.danceability, s.time_signature, s.year, s.writer, s.loudness
	'''

def search(request):
	if request.method == 'POST':
		form = SearchForm(request.POST)
		if (form.is_valid()):
			song = "\'" + form.cleaned_data['song_name'] + "\'"
			artist = "\'" + form.cleaned_data['artist_name'] + "\'"
			genre = "\'" + form.cleaned_data['genre_name'] + "\'"
			album = "\'" + form.cleaned_data['album_name'] + "\'"
			strt_yr =  form.cleaned_data['strt_yr'] 
			end_yr =  form.cleaned_data['end_yr'] 
			#run query
			query = get_search_query(song, artist, genre, album, strt_yr, end_yr)
			cursor = connection.cursor()					
			query = '''
			SELECT s.song_id, s.title, s.song_key, s.duration, s.energy, s.tempo, 
			s.danceability, s.time_signature, s.year, s.writer, s.loudness,g.genre_id, 
			g.label, art.artist_id, art.artist_name, a.album_id, a.album_name, s.year
			FROM tunesApp_song s 
			LEFT OUTER JOIN tunesapp_song_song_genres bt ON s.song_id = bt.song_id
			LEFT OUTER JOIN tunesapp_song_song_albums ai ON s.song_id = ai.song_id
			LEFT OUTER JOIN tunesapp_song_song_artists pl ON s.song_id = pl.song_id
			INNER JOIN tunesapp_genre g on bt.genre_id = g.genre_id
			INNER JOIN tunesapp_album a on ai.album_id = a.album_id
			INNER JOIN tunesapp_artist art on pl.artist_id = art.artist_id
			tunesapp_genre g, tunesapp_album a, tunesapp_artist art
			WHERE s.title LIKE IF(songStr is NULL, '%', CONCAT('%',songStr,'%')) 
			AND g.label LIKE IF(genreStr is NULL, '%', CONCAT('%',genreStr,'%')) 
			AND art.artist_name LIKE IF(artistStr is NULL, '%', CONCAT('%',artistStr,'%')) 
			AND a.album_name LIKE IF(albumStr IS NULL, '%', CONCAT('%',albumStr,'%'))
			#S.year between year1Input and IF(year1Input = 0, 3000, IF(year2Input = 0, year1Input, year2Input))
			GROUP BY s.song_id
			LIMIT 15;
			'''
			loggedInUser = request.user
			# Replace variable names with user inputs from the client
			query = query.replace('songStr',song)
			query = query.replace('genreStr',genre)
			query = query.replace('artistStr',artist)
			query = query.replace('albumStr',album)
			query = query.replace('year1Input',str(strt_yr))
			query = query.replace('year2Input',str(end_yr))
			print(query)
			cursor.execute(query)
			transactions = [to_string(x) for x in cursor.fetchall()]
			keys = ['song_id', 'title', 'song_key','duration','energy','tempo',
			'danceability','time_signature','year','writer','loudness', 'genre_id,',
			'label','artist_id','artist_name','album_id','album_name','year']
			# corresponding numeric value for each key to be used to populate dictionary
			countLst = range(len(keys))
			tempDict = {}
			masterList = []
			for tup in transactions:
				for i in countLst:
					tempDict[keys[i]] = tup[i]
				masterList.append(tempDict)
				tempDict = {}
			return render(request, 'results.html', {'masterList':masterList}) 
	else:
		form = SearchForm()
		return render(request, 'search.html')

#NEED TO FINISH THIS BY PRINTING/PARSING OUT KWARGS
def album_info(request, **kwargs):
	cursor = connection.cursor()
	print(kwargs)
	album_id = 0; #UPDATE THIS WITH PARSED OUT FIELD FROM KWARGS
	query = '''
	SELECT s.title,a.album_name,ai.album_id
	FROM Album a, Appears_in ai, Song s
	WHERE a.album_id = ai.album_id and ai.song_id = s.song_id and a.album_id = %s;
	'''
	cursor.execute(query,[album_id])
	transactions = [to_string(x) for x in cursor.fetchall()]
	keys = ['title','album_name','album_id']
	# corresponding numeric value for each key to be used to populate dictionary
	countLst = range(len(keys))
	tempDict = {}
	masterList = []
	for tup in transactions:
		for i in countLst:
			tempDict[keys[i]] = tup[i]
		masterList.append(tempDict)
		tempDict = {}
	return render(request, 'album_info.html',{'masterList':masterList})
