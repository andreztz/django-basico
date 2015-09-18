import time

from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'entrega/pedidos.html')
