from django.shortcuts import render

# Create your views here.

def home(request):
	"""The home page for the myTunes app."""
	return render (request, 'base.html')
	
def favorites(request):
	"""Favorites landing page."""
	return render(request, 'base.html')
	
def favSongs(request):
	"""Favorite songs for the user."""
	return render(request, 'base.html')
	
def favArtists(request):
	"""Favorite artists for the user."""
	return render(request, 'base.html')
	
def favGenres(request):
	"""Favorite genres for the user."""
	return render(request, 'base.html')
