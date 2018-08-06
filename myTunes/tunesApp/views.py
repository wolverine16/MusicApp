from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.db import connection
from django.forms import formset_factory
from .forms import SearchForm, SearchResults
from tunesApp.models import Song, Song_Likes

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
	s.loudness, sl.count, sl.rating, sl.id,al.album_name, 
	art.artist_name, g.label
	FROM auth_user u, tunesapp_song_likes sl, tunesapp_song s, 
	tunesapp_song_song_albums sal LEFT OUTER JOIN tunesapp_albums al
	ON sal.album_id = al.album_id, 
	tunesapp_song_song_artists sart, LEFT OUTER JOIN tunesapp_artists art
	on sart.artist_id = art.artist_id,
	tunesapp_song_song_genres sg LEFT OUTER JOIN tunesapp_genre g
	on sg.genre_id = g.genre_id
	WHERE u.id = sl.user_id_id and sl.song_id_id = s.song_id and u.username = %s
	and sl.song_id_id = sal.song_id and sl.song_id_id = sart.song_id 
	and sl.song_id_id = sg.song_id
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
		if (form.is_valid() and form.has_changed()):
			song = form.cleaned_data['song_name'] 
			artist = form.cleaned_data['artist_name'] 
			genre = form.cleaned_data['genre_name'] 
			album = form.cleaned_data['album_name'] 
			strt_yr = form.cleaned_data['strt_yr'] 
			end_yr = form.cleaned_data['end_yr'] 
			
			#dynamically construct and run query 
			cursor = connection.cursor()					
			
			query = '''
			SELECT s.song_id, s.title, s.song_key, s.duration, s.energy, s.tempo, 
			s.danceability, s.time_signature, s.year, s.writer, s.loudness,
			g.genre_id, g.label, art.artist_id, art.artist_name, a.album_id, a.album_name
			FROM tunesapp_song s 
			LEFT OUTER JOIN tunesapp_song_song_genres bt ON s.song_id = bt.song_id
			LEFT OUTER JOIN tunesapp_song_song_albums ai ON s.song_id = ai.song_id
			LEFT OUTER JOIN tunesapp_song_song_artists pl ON s.song_id = pl.song_id
			LEFT OUTER JOIN tunesapp_genre g on bt.genre_id = g.genre_id
			LEFT OUTER JOIN tunesapp_album a on ai.album_id = a.album_id
			LEFT OUTER JOIN tunesapp_artist art on pl.artist_id = art.artist_id
			WHERE '''
			conditions = ''
			queryTail = 'GROUP BY s.song_id LIMIT 15;'
			queryFieldList = [song, genre, artist, album, strt_yr, end_yr]
			nonNullIndices = []

			#get all non-null indices. Order defiend by queryFIeldList
			for num in range(queryFieldList):
				if queryFieldList[num] != '':
					nonNullIndices.append(num)

			# append all but the last one. 
			for num in range(len(nonNullIndices) - 1):
				if nonNullIndices[num] == 0:
					conditions += 's.title LIKE IF({0} is NULL, '%', CONCAT('%',{0},'%')) \nAND'.format("\'" + song + "\'")
				elif nonNullIndices[num] == 1:
					conditions += 'g.label LIKE IF({0} is NULL, '%', CONCAT('%',{0},'%')) \n AND'.format("\'" + genre + "\'")
				elif nonNullIndices[num] == 2:
					conditions += 'art.artist_name LIKE IF({0} is NULL, '%', CONCAT('%',{0},'%')) \n AND'.format("\'" + artist + "\'")
				elif nonNullIndices[num] == 3:
					conditions += 'a.album_name LIKE IF({0} IS NULL, '%', CONCAT('%',{0},'%')) \n AND'.format("\'" + album + "\'")
				# elif nonNullIndices[num] == 4:


			#handle last condition 
			lastIndex = nonNullIndices[len(nonNullIndices) - 1]
			if lastIndex == 0:
				conditions += 's.title LIKE IF({0} is NULL, '%', CONCAT('%',{0},'%'))'.format("\'" + song + "\'")
			elif lastIndex == 1:
				conditions += 'g.label LIKE IF({0} is NULL, '%', CONCAT('%',{0},'%')) \n AND'.format("\'" + genre + "\'")
			elif lastIndex == 2:
				conditions += 'art.artist_name LIKE IF({0} is NULL, '%', CONCAT('%',{0},'%')) \n AND'.format("\'" + artist + "\'")
			elif lastIndex == 3:
				conditions += 'a.album_name LIKE IF({0} IS NULL, '%', CONCAT('%',{0},'%')) \n AND'.format("\'" + album + "\'")
			# elif lastIndex == 4:
				# do something
			# elif lastIndex == 5:
				# do something

			# merge them all
			query = query + conditions + queryTail
			loggedInUser = request.user

			print(query)
			cursor.execute(query)
			transactions = [to_string(x) for x in cursor.fetchall()]
			keys = ['song_id', 'title', 'song_key','duration','energy','tempo',
			'danceability','time_signature','year','writer','loudness', 'genre_id',
			'label','artist_id','artist_name','album_id','album_name']

			# !!!TO DO: SAVE search result information into search model!!!

			# corresponding numeric value for each key to be used to populate dictionary
			countLst = range(len(keys))
			tempDict = {}
			masterList = []
			for tup in transactions:
				for i in countLst:
					tempDict[keys[i]] = tup[i]
				masterList.append(tempDict)
				tempDict = {}

			srch_formset = SearchResultsFormset(masterList)
			context = {'search_formset' : srch_formset}
			return render(request, 'results.html', context) 
	else:
		form = SearchForm()
		return render(request, 'search.html')


def results(request):
	
	user = request.user

	SearchResultsFormset = formset_factory(SearchResults)

	if request.method == POST:
		srch_results = SearchResultsFormset(request.POST)	

		if srch_results.is_valid():
			for one_line in srch_results:
				song_id = one_line.cleaned_data.get('song_id')
				is_add2fav = one_line.cleaned_data.get('add_to_fav')
				if is_add2fav:
					one_sg = Song.objects.get(pk=song_id)
					sg_likes = Song_Likes(song_id=one_sg, user_id=user)
					sg_likes.save()

		return HttpResponseRedirect('/favorites/songs')
	else:
		form = SearchResults()
		return render(request, 'results.html')

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