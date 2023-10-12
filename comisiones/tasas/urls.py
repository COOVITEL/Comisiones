from django.urls import path
from . import views


urlpatterns = [
    path("", views.comisiones, name="types_comisiones"),
    path("cdats/", views.cdats, name="cdats"),
    path("cooviahorros/", views.cooviahorro, name="cooviahorros"),
    path("ahorrovista/", views.ahorrovista, name="ahorrovista"),
]