from django.shortcuts import render
from django.db import connection
import datetime
import decimal

# Create your views here.

def home(request):
	"""The home page for the myTunes app."""
	return render (request, 'home.html')
	
def favorites(request):
	"""Favorites landing page."""
	return render(request, 'favorites_general.html')
	
def favSongs(request):
	"""Favorite songs for the user."""
	cursor = connection.cursor()
	cursor.execute('SELECT * FROM auth_user')
	transactions = [to_string(x) for x in cursor.fetchall()]
	#print(transactions)
	#transactions = [{"id":1},{"id":2}]
	keys = ['id','password','last_login','is_superuser',
	'username','first_name','last_name','email','is_staff',
	'is_active','date_joined']
	countLst = range(11)
	tempDict = {}
	masterList = []
	for tup in transactions:
		for i in countLst:
			tempDict[keys[i]] = tup[i]
		masterList.append(tempDict)
	print(masterList)
	return render(request, 'favorite_songs.html',{"masterList":masterList})

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
	return render(request, 'favorite_artists.html')
	
def favGenres(request):
	"""Favorite genres for the user."""
	return render(request, 'favorite_genres.html')
	
def test(request):
	"""Test page."""
	return render(request, 'test.html')
