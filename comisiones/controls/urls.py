from django.urls import path
from . import views

urlpatterns = [
    path("", views.welcome, name="welcome"),
    path("asesores/", views.asesores, name="asesores"),
    path("sucursales/", views.sucursales, name="sucursales"),
    path("createasesor/", views.createasesor, name="createasesor"),
    path("createsucursal/", views.createsucursal, name="createsucursal"),
    path("deleteasesor/<int:id>", views.deleteasesor, name="deleteasesor"),
    path("deletesucursal/<int:id>", views.deleteSucursal, name="deletesucursal"),
    path("comisiones/<str:name>", views.comisiones, name="comisionesAsesor"),
]