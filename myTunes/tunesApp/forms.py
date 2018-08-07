from django import forms
from django.forms import formset_factory
from django.forms.formsets import BaseFormSet

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
	
class GenreFavsForm(forms.Form):
	genre_id = forms.IntegerField(label='genre_id', required=False, widget=forms.HiddenInput())
	genre_label = forms.CharField(label='genre_label', required=False, widget=forms.HiddenInput())
	gl_id = forms.IntegerField(label='gl_id', widget=forms.HiddenInput())
	gl_delete = forms.BooleanField(initial=False, label='gl_delete', required=False)
	genre_rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label='genre_rating')
	
	
class BaseGenreFavsFormSet(BaseFormSet):
	def clean(self):
		"""Validate that rating is only between 0 and 10"""
		if any(self.errors):
			return
			
		for form in self.forms:
			if form.cleaned_data:
				rating = form.cleaned_data['genre_rating']
				
				if rating < 1 or rating > 10:
					raise forms.ValidationError('Rating must be between 1 and 10.', code='wrong_rating')
				

class ArtistFavsForm(forms.Form):
	artist_id = forms.CharField(label='artist_id', required=False, widget=forms.HiddenInput())
	artist_name = forms.CharField(label='artist_name', required=False, widget=forms.HiddenInput())
	al_id = forms.IntegerField(label='al_id', widget=forms.HiddenInput())
	al_delete = forms.BooleanField(initial=False, label='gl_delete', required=False)
	artist_rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label='artist_rating')
	
	
class BaseArtistFavsFormSet(BaseFormSet):
	def clean(self):
		"""Validate that rating is only between 0 and 10"""
		if any(self.errors):
			return
			
		for form in self.forms:
			if form.cleaned_data:
				rating = form.cleaned_data['artist_rating']
				
				if rating < 1 or rating > 10:
					raise forms.ValidationError('Rating must be between 1 and 10.', code='wrong_rating')
	

class SongFavsForm(forms.Form):
	song_id = forms.CharField(label='song_id', required=False, widget=forms.HiddenInput())
	song_title = forms.CharField(label='song_title', required=False, widget=forms.HiddenInput())
	song_key = forms.IntegerField(label='song_key', required=False, widget=forms.HiddenInput())
	duration = forms.DecimalField(label='duration', required=False, widget=forms.HiddenInput())
	energy = forms.DecimalField(label='energy', required=False, widget=forms.HiddenInput())
	tempo = forms.DecimalField(label='tempo', required=False, widget=forms.HiddenInput())
	loudness = forms.DecimalField(label='loudness', required=False, widget=forms.HiddenInput())
	danceability = forms.DecimalField(label='danceability', required=False, widget=forms.HiddenInput())
	time_sig = forms.IntegerField(label='time_signature', required=False, widget=forms.HiddenInput())
	writer = forms.CharField(label='writer', required=False, widget=forms.HiddenInput())
	genre_id = forms.IntegerField(label='genre_id', required=False, widget=forms.HiddenInput())
	genre_label = forms.CharField(label='genre_label', required=False, widget=forms.HiddenInput())
	artist_id = forms.CharField(label='artist_id', required=False, widget=forms.HiddenInput())
	artist_name = forms.CharField(label='artist_name', required=False, widget=forms.HiddenInput())
	album_id = forms.IntegerField(label='album_id', required=False, widget=forms.HiddenInput())
	album_name = forms.CharField(label='album_name', required=False, widget=forms.HiddenInput())
	year = forms.IntegerField(label='year', required=False, widget=forms.HiddenInput())
	sl_id = forms.IntegerField(label='sl_id', widget=forms.HiddenInput())
	sl_delete = forms.BooleanField(initial=False, label='sl_delete', required=False)
	sl_count = forms.IntegerField(label='sl_count', required=False, widget=forms.HiddenInput())
	song_rating = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}), label='song_rating')
	
	
	#song_id = forms.CharField(max_length = 30, required = False, widget = forms.HiddenInput())
	#title = forms.CharField(label = 'song', max_length = 150, required = False)
	#genre_id = forms.IntegerField(required = False, widget = forms.HiddenInput())
	#label = forms.CharField(label = 'genre', max_length = 150, required = False)
	#artist_id = forms.CharField(max_length = 30, required = False, widget = forms.HiddenInput())
	#artist_name = forms.CharField(label = 'artist', max_length = 150)
	#album_id = forms.IntegerField(required = False, widget = forms.HiddenInput())
	#album_name = forms.CharField(label = 'album', max_length = 150, required = False)
	#year = forms.IntegerField(label = 'year')

	
class BaseSongFavsFormSet(BaseFormSet):
	def clean(self):
		"""Validate that rating is only between 0 and 10"""
		if any(self.errors):
			return
			
		for form in self.forms:
			if form.cleaned_data:
				rating = form.cleaned_data['artist_rating']
				
				if rating < 1 or rating > 10:
					raise forms.ValidationError('Rating must be between 1 and 10.', code='wrong_rating')
