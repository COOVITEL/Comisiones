from django.urls import path
from . import views


urlpatterns = [
    path("", views.crecimientoBase, name="baseSocial"),
    path("createCrecimientoBase/", views.createCrecimientoBase, name="createBase"),
    path("updateCrecimientoBase/<int:id>", views.updateCrecimientoBase, name="updateBase"),
    path("deleteCrecimientoBase/<int:id>", views.deleteAhorrovista, name="deleteBase"),
]
