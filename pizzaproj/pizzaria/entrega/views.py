import time

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from entrega import models

# nossa primeira view
def relogio(request):
    hora = time.strftime('%H:%M:%S')
    return HttpResponse(hora)

def relogio_html(request):
    hora = time.strftime('%H:%M:%S')
    contexto = {'hora': hora}
    return render(request, 'entrega/hora.html', contexto)

def pedidos(request):
    """view que mostra o template pedidos.html"""
    res = models.Pedido.objects.all()
    contexto = {'pedidos': res}
    return render(request, 'entrega/pedidos.html',
                  contexto)

class ListaPedidos(ListView):
    model = models.Pedido
    #queryset = models.Pedido.objects.filter(partida__???=True)

class DetalhePedido(DetailView):
    model = models.Pedido
