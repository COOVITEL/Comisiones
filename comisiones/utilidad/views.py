from django.shortcuts import render, redirect
from .models import Utilidad


def utilidad(request):
    """"""
    dates = Utilidad.objects.all()
    return render(request, "utilidad.html", {"dates": dates})

def createUtilidad(request):
    """"""
    if request.method == 'POST':
        rangoMin = request.POST['rangoMin']
        rangoMax = request.POST['rangoMax']
        small = request.POST['small']
        medium = request.POST['medium']
        big = request.POST['big']
        create = Utilidad(rangoMin=rangoMin, rangoMax=rangoMax, small=small, medium=medium, big=big)
        create.save()
        return redirect("utilidad")
    return render(request, "createUtilidad.html")

def updateUtilidad(request, id):
    """"""
    uti = Utilidad.objects.get(id=id)
    if request.method == 'POST':
        uti.rangoMin = request.POST['rangoMin']
        uti.rangoMax = request.POST['rangoMax']
        uti.small = request.POST['small']
        uti.medium = request.POST['medium']
        uti.big = request.POST['big']
        uti.save()
        return redirect("utilidad")
    return render(request, "updateUtilidad.html", {"uti": uti})

def deleteUtilidad(request, id):
    """"""
    uti = Utilidad.objects.get(id=id)
    uti.delete()
    return redirect("utilidad")
