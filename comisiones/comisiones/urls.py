
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("controls.urls")),
    path("afiliaciones/", include("afiliaciones.urls")),
    path("colocaciones/", include("colocaciones.urls")),
    path("comisiones/", include("tasas.urls")),
    path("cdats/", include("cdats.urls")),
    path("cooviahorro/", include("cooviahorro.urls")),
    path("ahorrovista/", include("ahorrovista.urls")),
    path("crecimientoBaseSocial/", include("baseSocial.urls")),
    path('admin/', admin.site.urls),
]
