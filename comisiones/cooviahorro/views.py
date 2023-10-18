from django.shortcuts import render, redirect
from .models import Cooviahorro


def cooviahorro(request):
    """ This view return all cooviahorros created """
    coovi = Cooviahorro.objects.all()
    return render(request, "cooviahorros.html", {"coovi": coovi})

def createCooviahorro(request):
    """ This view create a new cooviahorro """
    if request.method == 'POST':
        monto = request.POST['monto']
        value = request.POST['value']
        create = Cooviahorro(monto=monto , value=value)
        create.save()
        return redirect("cooviahorros")
    return render(request, "createcooviahorro.html")

def updateCooviahorro(request, id):
    """This method update a cooviahorro
        id is a number of the object.id
    """
    coovi = Cooviahorro.objects.get(id=id)
    if request.method == 'POST':
        coovi.monto = request.POST['monto']
        coovi.value = request.POST['value']
        coovi.save()
        return redirect("cooviahorros")
    return render(request, "updatecooviahorro.html", {"coovi": coovi})

def deleteCooviahorro(request, id):
    """ This view delete a cooviahorro
        with the id take the object to delete.
    """
    coovi = Cooviahorro.objects.get(id=id)
    coovi.delete()
    return redirect("cooviahorros")
