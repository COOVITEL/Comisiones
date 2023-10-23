from django.conf import settings
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
    path("cartera/", include("cartera.urls")),
    path("crecimientoCdat/", include("crecimientoCDAT.urls")),
    path("crecimientoCooviahorro/", include("crecimientoCooviahorro.urls")),
    path("captacionAhorroVista/", include("captacionAhorroVista.urls")),
    path("utilidad/", include("utilidad.urls")),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)