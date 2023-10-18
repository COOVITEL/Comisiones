from django.urls import path
from . import views


urlpatterns = [
    path("", views.ahorrovista, name="ahorrovista"),
    path("createahorrovista", views.createAhorrovista, name="createahorro"),
    path("updateahorrovista/<int:id>", views.updateAhorrovista, name="updateahorro"),
    path("deleteahorrovista/<int:id>", views.deleteAhorrovista, name="deleteahorro"),
]