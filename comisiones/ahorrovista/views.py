from django.shortcuts import render, redirect
from .models import AhorroVista


def ahorrovista(request):
    """"""
    ahorros = AhorroVista.objects.all()
    return render(request, "ahorrovista.html", {"ahorros": ahorros})

def createAhorrovista(request):
    """"""
    if request.method == 'POST':
        since = request.POST['since']
        until = request.POST['until']
        porcentaje = request.POST['porcentaje']
        create = AhorroVista(since=since, until=until, porcentaje=porcentaje)
        create.save()
        return redirect("ahorrovista")
    return render(request, "createahorrovista.html")

def updateAhorrovista(request, id):
    """"""
    ahorro = AhorroVista.objects.get(id=id)
    if request.method == 'POST':
        ahorro.since = request.POST['since']
        ahorro.until = request.POST['until']
        ahorro.porcentaje = request.POST['porcentaje']
        ahorro.save()
        return redirect("ahorrovista")
    return render(request, "updateahorrovista.html", {"ahorro": ahorro})

def deleteAhorrovista(request, id):
    """"""
    ahorro = AhorroVista.objects.get(id=id)
    ahorro.delete()
    return redirect("ahorrovista")
