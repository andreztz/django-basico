"""
entrega/urls.py
"""
from django.conf.urls import url

from entrega import views

urlpatterns = [
    url(r'^hora$', views.relogio),
    url(r'^hora2$', views.relogio_html),
    url(r'^pedidos$', views.pedidos),
]
