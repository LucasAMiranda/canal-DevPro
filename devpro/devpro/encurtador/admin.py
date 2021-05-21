from django.contrib import admin
from devpro.encurtador.models import UrlRedirect, UrlLog

#Herda da classe admin
@admin.register(UrlRedirect)
class UrlRedirectAdmin(admin.ModelAdmin):

    #colunas do nosso data base no Admin
    list_display = ('destino', 'slug', 'criado_em', 'atualizado_em')

@admin.register(UrlLog)
class UrlLogAdmin(admin.ModelAdmin):

    list_display = ('origem', 'criado_em', 'user_agente', 'host', 'ip', 'url_redirect')

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False



