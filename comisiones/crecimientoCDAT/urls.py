from django.urls import path
from . import views


urlpatterns = [
    path("", views.crecimientoCdat, name="crecimientoCdat"),
    path("createCrecimientoCdat", views.createCrecimientoCdat, name="createCrecimientoCdat"),
    path("updateCrecimientoCdat/<int:id>", views.updateCrecimientoCdat, name="updateCrecimientoCdat"),
    path("deleteCrecimientoCdat/<int:id>", views.deleteCrecimientoCdat, name="deleteCrecimientoCdat"),
]
