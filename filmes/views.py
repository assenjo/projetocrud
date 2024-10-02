from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from filmes.forms import FilmeForm, PlaylistForm
from filmes.models import Filmes, Playlist 

class PlaylistListView(ListView):
    model = Playlist
    template_name = 'playlist/playlist_list.html'
    paginate_by = 5
    context_object_name = 'playlists'
    queryset = Playlist.objects.order_by('-id')

class PlaylistDetailView(DetailView):
    model = Playlist 
    template_name = 'playlist/playlist_detail.html'
    context_object_name = 'playlists'

class PlaylistCreateView(CreateView):
    model = Playlist
    form_class = PlaylistForm
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')

class PlaylistUpdateView(UpdateView):
    model = Playlist
    fields = ['nome', 'filmes']
    template_name = 'playlist/playlist_form.html'
    success_url = reverse_lazy('playlist_list')

class PlaylistDeleteView(DeleteView):
    model = Playlist
    success_url = reverse_lazy('playlist_list')   

    #filme crud

class FilmeListView(ListView):
    model = Filmes
    template_name = 'filmes/filme_list.html'

class FilmeCreateView(CreateView):
    model = Filmes
    form_class = FilmeForm
    template_name = 'filmes/filme_form.html'
    success_url = reverse_lazy('filme_list')    

class FilmeDetailView(DetailView):
    model = Filmes
    form_class = FilmeForm
    template_name = 'filmes/filmes_form.html'

class FilmeUpdateView(UpdateView):
    model = Filmes
    form_class = FilmeForm
    template_name = 'filmes/filme_form.html'
    success_url = reverse_lazy ('filme_list')

class FilmeDeleteView(DeleteView):
    model = Filmes
    template_name = 'filmes/filme_confirm_delete.html'
    success_url = reverse_lazy('filme_list') 
