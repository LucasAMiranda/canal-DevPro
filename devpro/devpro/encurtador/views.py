from django.shortcuts import render, redirect

from devpro.encurtador.models import UrlRedirect

def redirecionar(requisicao, slug):
    urlRedirect = UrlRedirect.objects.get(slug=slug)
    return redirect(urlRedirect.destino)
