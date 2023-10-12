from django.shortcuts import render, redirect
from .models import Colocaciones

# Create your views here.
def colocaciones(request):
    """"""
    int_ext = Colocaciones.objects.filter(type="InternosyExternos")
    masters = Colocaciones.objects.filter(type="Master")
    directores = Colocaciones.objects.filter(type="DirectoryCoordinador")
    return render(request, "colocaciones.html",{"internos": int_ext,
                                                "masters": masters,
                                                "directores": directores})

def createColocaciones(request):
    """"""
    if request.method == 'POST':
        tasaMin = request.POST['tasaMin']
        tasaMax = request.POST['tasaMax']
        since = request.POST['since']
        until = request.POST['until']
        value = request.POST['value']
        type = request.POST['type']
        create = Colocaciones(tasaMin=tasaMin,
                              tasaMax=tasaMax,
                              since=since,
                              until=until,
                              value=value,
                              type=type)
        create.save()
        return redirect("colocaciones")
    return render(request, "createcolocaciones.html")

def updateColocaciones(request, id):
    """"""
    col = Colocaciones.objects.get(id=id)
    context = {"col": col}
    if request.method == "POST":
        col.tasaMin = request.POST['tasaMin']
        col.tasaMax = request.POST['tasaMax']
        col.since = request.POST['since']
        col.until = request.POST['until']
        col.value = request.POST['value']
        col.save()
        return redirect("colocaciones")
    return render(request, 'updatecolocaciones.html', context)

def deleteColocaciones(request, id):
    """"""
    colocacion = Colocaciones.objects.get(id=id)
    colocacion.delete()
    return redirect("colocaciones")
    