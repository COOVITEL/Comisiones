from django.urls import path
from . import views


urlpatterns = [
    path("", views.comisiones, name="types_comisiones"),
]