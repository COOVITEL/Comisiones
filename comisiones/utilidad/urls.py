from django.urls import path
from . import views


urlpatterns = [
    path("", views.utilidad, name="utilidad"),
    path("createUtilidad/", views.createUtilidad, name="createUtilidad"),
    path("updateUtilidad/<int:id>", views.updateUtilidad, name="updateUtilidad"),
    path("deleteUtilidad/<int:id>", views.deleteUtilidad, name="deleteUtilidad")
]
