from django.urls import path
from . import views


urlpatterns = [
    path("", views.crecimientoCooviahorro, name="crecimientoCooviahorro"),
    path("createCrecimientoCooviahorro", views.createCrecimientoCooviahorro, name="createCrecimientoCooviahorro"),
    path("updateCrecimientoCooviahorro/<int:id>", views.updateCrecimientoCooviahorro, name="updateCrecimientoCooviahorro"),
    path("deleteCrecimientoCooviahorro/<int:id>", views.deleteCrecimientoCooviahorro, name="deleteCrecimientoCooviahorro"),
]
