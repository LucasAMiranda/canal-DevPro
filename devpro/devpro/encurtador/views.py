from django.shortcuts import render, redirect

from devpro.encurtador.models import UrlRedirect, UrlLog

def relatorios(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    url_reduzida = requisicao.build_absolute_uri(f'/{slug}')
    context = {
        'reduce': url_redirect,
        'url_reduzida': url_reduzida,

    }
    return render(requisicao, 'encurtador/relatorio.html', context)

def redirecionar(requisicao, slug):
    url_redirect = UrlRedirect.objects.get(slug=slug)
    UrlLog.objects.create(
        origem=requisicao.META.get('HTTP_REFERER'),
        user_agente=requisicao.META.get('HTTP_USER_AGENT'),
        host=requisicao.META.get('HTTP_HOST'),
        ip=requisicao.META.get('REMOTE_ADDR'),
        url_redirect=url_redirect
    )
    return redirect(url_redirect.destino)
