from django.shortcuts import render, redirect
from .models import CrecimeintoBaseSocial


def crecimientoBase(request):
    """"""
    objs = CrecimeintoBaseSocial.objects.all()
    return render(request, "crecimientobase.html", {"objs": objs})

def createCrecimientoBase(request):
    """"""
    if request.method == 'POST':
        amount = request.POST['amount']
        value = request.POST['value']
        create = CrecimeintoBaseSocial(amount=amount, value=value)
        create.save()
        return redirect("baseSocial")
    return render(request, "createcrecimientobase.html")

def updateCrecimientoBase(request, id):
    """"""
    base = CrecimeintoBaseSocial.objects.get(id=id)
    if request.method == 'POST':
        base.amount = request.POST['amount']
        base.value = request.POST['value']
        base.save()
        return redirect("baseSocial")
    return render(request, "updatecrecimientobase.html", {"base": base})

def deleteAhorrovista(request, id):
    """"""
    base = CrecimeintoBaseSocial.objects.get(id=id)
    base.delete()
    return redirect("baseSocial")