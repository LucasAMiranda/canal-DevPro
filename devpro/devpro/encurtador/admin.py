from django.contrib import admin
from devpro.encurtador.models import UrlRedirect

#Herda da classe admin
@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):

    #colunas do nosso data base no Admin
    list_display = ('destino', 'slug', 'criado_em', 'atualizado_em')


