from django import forms.ModelF
from .models import MovieInfo

class MovieForm(ModelForm):
    class Meta:
        model = MovieInfo
        fields = '__all__'  # Maps to your model columns
