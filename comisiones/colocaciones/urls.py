from django.urls import path
from . import views


urlpatterns = [
    path("", views.colocaciones, name="colocaciones"),
    path("createcolocaciones", views.createColocaciones, name="createcol"),
    path("updatecolcoaciones/<int:id>", views.updateColocaciones, name="updatecol"),
    path("deletecolocaciones/<int:id>", views.deleteColocaciones, name="deletecol"),
]
