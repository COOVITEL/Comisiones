from django.urls import path
from . import views


urlpatterns = [
    path("", views.cartera, name="cartera"),
    path("createCartera/", views.createCartera, name="createcartera"),
    path("updateCartera/<int:id>", views.updateCartera, name="updatecartera"),
    path("deleteCartera/<int:id>", views.deleteCartera, name="deletecartera"),
]
