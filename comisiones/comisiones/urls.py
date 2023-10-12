
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("controls.urls")),
    path("afiliaciones/", include("afiliaciones.urls")),
    path("colocaciones/", include("colocaciones.urls")),
    path("comisiones/", include("tasas.urls")),
    path('admin/', admin.site.urls),
]
