from django.urls import path
from . import views


urlpatterns = [
    path("comisiones/", views.comisiones, name="types_comisiones"),
    path("afiliaciones/", views.afiliaciones, name="afiliaciones"),
    path("colocaciones/", views.colocaciones, name="colocaciones"),
    path("cdats/", views.cdats, name="cdats"),
    path("cooviahorros/", views.cooviahorro, name="cooviahorros"),
    path("ahorrovista/", views.ahorrovista, name="ahorrovista"),
]