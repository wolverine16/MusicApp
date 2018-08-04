from django.shortcuts import render
from django.db import connection
import datetime
import decimal

# Create your views here.

def home(request):
	"""The home page for the myTunes app."""
	return render(request, 'home.html')
	
def searchApp(request):
	"""Initial page for entering search parameters."""
	# Pass in form fields
	# Process POST events
	# Validate entered data
	return render(request, 'search.html')
	
def favorites(request):
	"""Favorites landing page."""
	return render(request, 'favorites_general.html')
	
def favSongs(request):
	"""Favorite songs for the user."""
	cursor = connection.cursor()
	#raw sql to be executed:
	query = '''
	SELECT s.song_id, s.title, s.song_key, s.duration, s.energy, 
	s.tempo, s.danceability, s.time_signature, s.year, s.writer, 
	s.loudness, sl.count, sl.rating
	FROM auth_user u, tunesapp_song_likes sl, tunesapp_song s
	WHERE u.username = sl.user_id_id and sl.song_id_id = s.song_id
	ORDER BY sl.rating DESC;
	'''
	cursor.execute(query)
	transactions = [to_string(x) for x in cursor.fetchall()]
	#print(transactions)
	#transactions = [{"id":1},{"id":2}]
	keys = ['song_id','title','song_key','duration','energy',
	'tempo','danceability','time_signature','year','writer',
	'loudness','count','rating']
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
	query = '''
	SELECT a.artist_id, a.artist_name, al.rating
	FROM auth_user u, tunesapp_Artist_likes al, tunesapp_Artist a
	WHERE u.username = al.user_id_id and al.artist_id_id = a.artist_id
	ORDER BY al.rating DESC;
	'''
	cursor.execute(query)
	transactions = [to_string(x) for x in cursor.fetchall()]
	#print(transactions)
	#transactions = [{"id":1},{"id":2}]
	keys = ['artist_id','artist name','rating']
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
	query = '''
	SELECT g.genre_id, g.label, gl.rating
	FROM auth_user u, tunesapp_Genre_likes gl, tunesapp_Genre g
	WHERE u.id = gl.user_id_id and gl.genre_id_id = g.genre_id and gl.user_id_id = 5 
	ORDER BY gl.rating DESC
	'''
	cursor.execute(query)
	transactions = [to_string(x) for x in cursor.fetchall()]
	#print(transactions)
	#transactions = [{"id":1},{"id":2}]
	keys = ['genre_id', 'label', 'rating']
	# corresponding numeric value for each key to be used to populate dictionary
	countLst = range(len(keys))
	tempDict = {}
	masterList = []
	for tup in transactions:
		for i in countLst:
			tempDict[keys[i]] = tup[i]
		masterList.append(tempDict)
		tempDict = {}
	print(masterList)
	return render(request, 'favorite_genres.html',{'masterList':masterList})
	
def test(request):
	"""Test page."""
	return render(request, 'test.html')
