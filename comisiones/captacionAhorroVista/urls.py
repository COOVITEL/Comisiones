from django.urls import path
from . import views


urlpatterns = [
    path("", views.captacionAhorroVista, name="captacionesAhorro"),
    path("createCaptacionesAhorro/", views.createCaptacionAhorroVista, name="createcaptacionesAhorro"),
    path("updateCaptacionesAhorro/<int:id>", views.updateCaptacionAhorroVista, name="updatecaptacionesAhorro"),
    path("deleteCaptacionesAhorro/<int:id>", views.deleteCaptacionAhorroVista, name="deletecaptacionesAhorro"),
]
