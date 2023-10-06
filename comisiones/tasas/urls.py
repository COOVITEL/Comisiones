from django.urls import path
from . import views


urlpatterns = [
    path("comisiones/", views.comisiones, name="types_comisiones")
]