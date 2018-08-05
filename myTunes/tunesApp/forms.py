from django import forms

class SearchForm(forms.Form):
	song_name = forms.CharField(label = 'song', max_length = 150)
	artist_name = forms.CharField(label = 'artist', max_length = 150)
	genre_name = forms.CharField(label = 'genre', max_length = 150)
	album_name = forms.CharField(label='album', max_length = 150)
	strt_yr = forms.CharField(label = 'year', max_length = 150)