from django.shortcuts import render, redirect
from .models import CaptacionAhorroVista


def captacionAhorroVista(request):
    """"""
    ahorros = CaptacionAhorroVista.objects.all()
    return render(request, "capAhorroVista.html", {"ahorros": ahorros})

def createCaptacionAhorroVista(request):
    """"""
    if request.method == 'POST':
        since = request.POST['since']
        until = request.POST['until']
        value = request.POST['value']
        create = CaptacionAhorroVista(since=since, until=until, value=value)
        create.save()
        return redirect("captacionesAhorro")
    return render(request, "createCapAhorroVista.html")

def updateCaptacionAhorroVista(request, id):
    """"""
    ahorro = CaptacionAhorroVista.objects.get(id=id)
    if request.method == 'POST':
        ahorro.since = request.POST['since']
        ahorro.until = request.POST['until']
        ahorro.value = request.POST['value']
        ahorro.save()
        return redirect("captacionesAhorro")
    return render(request, "updateCapAhorroVista.html", {"ahorro": ahorro})

def deleteCaptacionAhorroVista(request, id):
    """"""
    ahorro = CaptacionAhorroVista.objects.get(id=id)
    ahorro.delete()
    return redirect("captacionesAhorro")