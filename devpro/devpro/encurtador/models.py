from django.db import models

class UrlRedirect(models.Model): #Herda da classe Modelo: models.Model
    destino = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True) #Cria um restrição no banco de dados
    criado_em = models.DateTimeField(auto_now_add=True) #Cria a hora atual
    atualizado_em = models.DateTimeField(auto_now=True) #Cria a data e hora já atualizado

    def __str__(self):
        return f"UrlRedirect para {self.destino}"

