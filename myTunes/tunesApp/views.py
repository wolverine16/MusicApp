from django.shortcuts import render

# Create your views here.

def home(request):
	"""The home page for the myTunes app."""
	return render (request, 'home.html')
	
def favorites(request):
	"""Favorites landing page."""
	return render(request, 'favorites_general.html')
	
def favSongs(request):
	"""Favorite songs for the user."""
	return render(request, 'favorite_songs.html')
	
def favArtists(request):
	"""Favorite artists for the user."""
	return render(request, 'favorite_artists.html')
	
def favGenres(request):
	"""Favorite genres for the user."""
	return render(request, 'favorite_genres.html')
	
def test(request):
	"""Test page."""
	return render(request, 'test.html')
