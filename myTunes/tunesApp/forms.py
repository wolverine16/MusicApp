from django import forms
from django.forms import formset_factory

class SearchForm(forms.Form):
	song_name = forms.CharField(label = 'song', max_length = 150, required = False)
	artist_name = forms.CharField(label = 'artist', max_length = 150, required = False)
	genre_name = forms.CharField(label = 'genre', max_length = 150, required = False)
	album_name = forms.CharField(label='album', max_length = 150, required = False)
	strt_yr = forms.IntegerField(label = 'strt_year', required = False)
	end_yr = forms.IntegerField(label = 'end_year', required = False)


class SearchResults(forms.Form):
	song_id = forms.CharField(max_length = 30, required = False, widget = forms.HiddenInput())
	title = forms.CharField(label = 'song', max_length = 150, required = False)
	genre_id = forms.IntegerField(required = False, widget = forms.HiddenInput())
	label = forms.CharField(label = 'genre', max_length = 150, required = False)
	artist_id = forms.CharField(max_length = 30, required = False, widget = forms.HiddenInput())
	artist_name = forms.CharField(label = 'artist', max_length = 150)
	album_id = forms.IntegerField(required = False, widget = forms.HiddenInput())
	album_name = forms.CharField(label = 'album', max_length = 150, required = False)
	year = forms.IntegerField(label = 'year')
	add_to_fav = forms.BooleanField(label = 'is_fav')
	
