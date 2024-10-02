from django.db import models
from django.core.validators import FileExtensionValidator

class Filmes(models.Model):
    titulo = models.CharField(max_length=100)
    produtora = models.CharField(max_length=100)
    atores = models.CharField(max_length=100)
    capa = models.ImageField(upload_to='capas/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str___(self):
        return f"{self.titulo} {self.atores}"
    
class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    filmes = models.ManyToManyField(Filmes)

    def __str__(self):
        return self.nome

