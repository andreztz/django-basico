"""
entrega/urls.py
"""
from django.conf.urls import url

from entrega import views

urlpatterns = [
    url(r'^hora', views.relogio),
]
