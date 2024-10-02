from django import forms 
from .models import Playlist, Filmes

class PlaylistForm(forms.ModelForm):
    class Meta:
        model = Playlist
        fields = '__all__'

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filmes
        fields = '__all__'