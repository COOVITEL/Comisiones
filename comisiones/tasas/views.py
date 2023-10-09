from django.shortcuts import render
from .models import Afiliaciones, Colocaciones, Cdats, Cooviahorro, AhorroVista


def comisiones(request):
    return render(request, "types_comisiones.html")

def afiliaciones(request):
    afiliacion = Afiliaciones.objects.all()
    return render(request, "afiliaciones.html", {"afiliacion": afiliacion})

def colocaciones(request):
    int_ext = Colocaciones.objects.filter(type="Internos, Externos")
    masters = Colocaciones.objects.filter(type="Master")
    directores = Colocaciones.objects.filter(type="Directores, Coordinadores")
    return render(request, "colocaciones.html",{"internos": int_ext,
                                                "masters": masters,
                                                "directores": directores})

def cdats(request):
    cdats = Cdats.objects.all()
    return render(request, "cdats.html", {"cdats": cdats})

def cooviahorro(request):
    coovi = Cooviahorro.objects.all()
    return render(request, "cooviahorros.html", {"coovi": coovi})

def ahorrovista(request):
    ahorros = AhorroVista.objects.all()
    return render(request, "ahorrovista.html", {"ahorros": ahorros})