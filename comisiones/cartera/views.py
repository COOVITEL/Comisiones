from django.shortcuts import render, redirect
from .models import Cartera


def cartera(request):
    """"""
    dates = Cartera.objects.all()
    return render(request, "cartera.html", {"dates": dates})

def createCartera(request):
    """"""
    if request.method == 'POST':
        tasaMin = request.POST['tasaMin']
        tasaMax = request.POST['tasaMax']
        sinde = request.POST['sinde']
        until = request.POST['until']
        value = request.POST['value']
        create = Cartera(tasaMin=tasaMin, tasaMax=tasaMax, sinde=sinde, until=until, value=value)
        create.save()
        return redirect("cartera")
    return render(request, "createcartera.html")

def updateCartera(request, id):
    """"""
    cartera = Cartera.objects.get(id=id)
    if request.method == 'POST':
        cartera.tasaMin = request.POST['tasaMin']
        cartera.tasaMax = request.POST['tasaMax']
        cartera.sinde = request.POST['sinde']
        cartera.until = request.POST['until']
        cartera.value = request.POST['value']
        cartera.save()
        return redirect("cartera")
    return render(request, "updatecartera.html", {"cartera": cartera})

def deleteCartera(request, id):
    """"""
    cartera = Cartera.objects.get(id=id)
    cartera.delete()
    return redirect("cartera")