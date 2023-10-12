from django.shortcuts import render, redirect
from .models import Cdats, Cooviahorro, AhorroVista


def comisiones(request):
    """
    This function create a render that conteion the
    diferents types of the comision.
    """
    return render(request, "types_comisiones.html")

def cdats(request):
    cdats = Cdats.objects.all()
    return render(request, "cdats.html", {"cdats": cdats})

def cooviahorro(request):
    coovi = Cooviahorro.objects.all()
    return render(request, "cooviahorros.html", {"coovi": coovi})

def ahorrovista(request):
    ahorros = AhorroVista.objects.all()
    return render(request, "ahorrovista.html", {"ahorros": ahorros})