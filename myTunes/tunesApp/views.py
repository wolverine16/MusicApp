from django.shortcuts import render

# Create your views here.

def home(request):
	"""The home page for the myTunes app."""
	return render (request, 'base.html')
