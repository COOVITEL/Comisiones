from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import CrecimientoCooviahorro


def crecimientoCooviahorro(request):
    """"""
    coovis = CrecimientoCooviahorro.objects.all()
    return render(request, "crecimientoCoovi.html", {"coovis": coovis})

def createCrecimientoCooviahorro(request):
    """"""
    if request.method == 'POST':
        since = request.POST['since']
        value = request.POST['value']
        create = CrecimientoCooviahorro(since=since, value=value)
        create.save()
        return redirect("crecimientoCooviahorro")
    return render(request, "createcrecimientoCoovi.html")

def updateCrecimientoCooviahorro(request, id):
    """"""
    coovi = CrecimientoCooviahorro.objects.get(id=id)
    if request.method == 'POST':
        coovi.since = request.POST['since']
        coovi.value = request.POST['value']
        coovi.save()
        return redirect("crecimientoCooviahorro")
    return render(request, "updatecrecimientoCoovi.html", {"coovi": coovi})

def deleteCrecimientoCooviahorro(request, id):
    """"""
    coovi = CrecimientoCooviahorro.objects.get(id=id)
    coovi.delete()
    return redirect("crecimientoCooviahorro")