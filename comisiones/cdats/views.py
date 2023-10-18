from django.shortcuts import render, redirect
from .models import Cdats

# Create your views here.
def cdats(request):
    """"""
    cdat = Cdats.objects.all()
    return render(request, 'cdats.html', {"cdats": cdat})

def createcdat(request):
    """"""
    if request.method == 'POST':
        since = request.POST['since']
        until = request.POST['until']
        value = request.POST['value']
        type = request.POST['type']
        create = Cdats(since=since, until=until, value=value,type=type)
        create.save()
        return redirect('cdats')
    return render(request, 'createcdat.html')

def updatecdat(request, id):
    """"""
    cdat = Cdats.objects.get(id=id)
    if request.method == 'POST':
        cdat.since = request.POST['since']
        cdat.until = request.POST['until']
        cdat.value = request.POST['value']
        cdat.save()
        return redirect("cdats")
    return render(request, 'updatecdat.html', {"cdat": cdat})

def deletecdat(request, id):
    """"""
    cdat = Cdats.objects.get(id=id)
    cdat.delete()
    return redirect("cdats")
