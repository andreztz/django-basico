import time

from django.shortcuts import render
from django.http import HttpResponse

# nossa primeira view
def relogio(request):
    hora = time.strftime('%H:%M:%S')
    return HttpResponse(hora)
