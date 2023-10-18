from django.urls import path
from . import views


urlpatterns = [
    path("", views.cooviahorro, name="cooviahorros"),
    path("createcooviahorro/", views.createCooviahorro, name="createcoovi"),
    path("updatecooviahorro/<int:id>", views.updateCooviahorro, name="updatecoovi"),
    path("deletecooviahorro/<int:id>", views.deleteCooviahorro, name="deletecoovi"),
]
