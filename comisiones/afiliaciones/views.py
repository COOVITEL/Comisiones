""" Model contein the function to afiliaciones """
from django.shortcuts import render, redirect
from .models import Afiliaciones


def afiliaciones(request):
    """
    This function return the case of the afiliaciones
    comison for the individual asesors.
    """
    afiliacion = Afiliaciones.objects.all()
    return render(request, "afiliaciones.html", {"afiliacion": afiliacion})

def createAfiliacion(request):
    """"""
    if request.method == 'POST':
        since = request.POST['since']
        until = request.POST['until']
        value = request.POST['value']
        create = Afiliaciones(since=since, until=until, value=value)
        create.save()
        return redirect("afiliaciones")
    return render(request, 'createafiliacion.html')

def updateafi(request, id):
    """
    This function update the afiliaciones
    comisions of the individual asesors.
    """
    afi = Afiliaciones.objects.get(id=id)
    context = {"afi": afi}
    if request.method == 'POST':
        afi.since = request.POST['since']
        afi.until = request.POST['until']
        afi.value = request.POST['value']
        afi.save()
        return redirect('afiliaciones')
    return render(request, 'updateafiliaciones.html', context)

def deleteafi(request, id):
    """ This function delete a afiliacion """
    afi = Afiliaciones.objects.get(id=id)
    afi.delete()
    return redirect('afiliaciones')
