"""
entrega/urls.py
"""
from django.conf.urls import url

from entrega import views

urlpatterns = [
    url(r'^hora$', views.relogio),
    url(r'^hora2$', views.relogio_html),
    url(r'^pedidos$', views.pedidos),
    url(r'^lped$', views.ListaPedidos.as_view(),
        name='lista_pedidos'),
    url(r'^ped/(?P<pk>\d+)$', views.DetalhePedido.as_view(),
        name='detalhe_pedido'),
]
