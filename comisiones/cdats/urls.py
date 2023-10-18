from django.urls import path
from . import views


urlpatterns = [
    path("", views.cdats, name="cdats"),
    path("createcdat/", views.createcdat, name="createcdat"),
    path("updatecdat/<int:id>", views.updatecdat, name="updatecdat"),
    path("deletecdat/<int:id>", views.deletecdat, name="deletecdat"),
]
