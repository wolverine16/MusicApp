from django import forms

class SearchForm(forms.Form):
	song_name = forms.CharField(label = 'song', max_length = 150, required = False)
	artist_name = forms.CharField(label = 'artist', max_length = 150, required = False)
	genre_name = forms.CharField(label = 'genre', max_length = 150, required = False)
	album_name = forms.CharField(label='album', max_length = 150, required = False)
	strt_yr = forms.IntegerField(label = 'strt_year', required = False)
	end_yr = forms.IntegerField(label = 'end_year', required = False)


class SearchResults(forms.Form):
	song_name = forms.CharField(label = 'song', max_length = 150)
	artist_name = forms.CharField(label = 'artist', max_length = 150)
	album_name = forms.CharField(label = 'album', max_length = 150)
	genre_name = forms.CharField(label = 'genre', max_length = 150)
	year = forms.IntegerField(label = 'year')
	add_to_fav = forms.BooleanField(label = 'is_fav')
