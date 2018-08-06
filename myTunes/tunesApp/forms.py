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
					

