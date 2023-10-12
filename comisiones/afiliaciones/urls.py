from django.urls import path
from . import views


urlpatterns = [
    path("", views.afiliaciones, name="afiliaciones"),
    path("createafiliacion", views.createAfiliacion, name="createafiliacion"),
    path("updateafiliacion/<int:id>", views.updateafi, name="updateafi"),
    path("deleteafiliacion/<int:id>", views.deleteafi, name="deleteafi"),
]
