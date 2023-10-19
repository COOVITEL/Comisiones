from django.shortcuts import render, redirect
from .models import CrecimientoCDAT


def crecimientoCdat(request):
    """"""
    cdats = CrecimientoCDAT.objects.all()
    return render(request, "crecimientoCdat.html", {"cdats": cdats})

def createCrecimientoCdat(request):
    """"""
    if request.method == 'POST':
        tasaMin = request.POST['tasaMin']
        tasaMax = request.POST['tasaMax']
        value = request.POST['value']
        create = CrecimientoCDAT(tasaMin=tasaMin, tasaMax=tasaMax, value=value)
        create.save()
        return redirect("crecimientoCdat")
    return render(request, "createcrecimientoCdat.html")

def updateCrecimientoCdat(request, id):
    """"""
    cdat = CrecimientoCDAT.objects.get(id=id)
    if request.method == 'POST':
        cdat.tasaMin = request.POST['tasaMin']
        cdat.tasaMax = request.POST['tasaMax']
        cdat.value = request.POST['value']
        cdat.save()
        return redirect("crecimientoCdat")
    return render(request, "updatecrecimientoCdat.html", {"cdat": cdat})

def deleteCrecimientoCdat(request, id):
    """"""
    cdat = CrecimientoCDAT.objects.get(id=id)
    cdat.delete()
    return redirect("crecimientoCdat")