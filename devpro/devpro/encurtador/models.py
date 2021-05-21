from django.db import models

class UrlRedirect(models.Model): #Herda da classe Modelo: models.Model
    destino = models.URLField(max_length=512)
    slug = models.SlugField(max_length=128, unique=True) #Cria um restrição no banco de dados
    criado_em = models.DateTimeField(auto_now_add=True) #Cria a hora atual
    atualizado_em = models.DateTimeField(auto_now=True) #Cria a data e hora já atualizado

    def __str__(self):
        return f"UrlRedirect para {self.destino}"

class UrlLog(models.Model):
     criado_em = models.DateTimeField(auto_now_add=True)
     origem = models.URLField(max_length=512, null=True, blank=True)
     user_agente = models.CharField(max_length=512, null=True, blank=True)
     host = models.CharField(max_length=512, null=True, blank=True)
     ip = models.GenericIPAddressField(null=True, blank=True)
     url_redirect = models.ForeignKey(UrlRedirect, models.DO_NOTHING, related_name='logs')