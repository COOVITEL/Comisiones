from django.shortcuts import render, redirect
from .models import Asesor, Sucursal

# Create your views here.

def welcome(request):
    return render(request, "layout.html")

def asesores(request):
    ciudad = Sucursal.objects.all()
    city = request.GET.get("ciudad", None)
    todos = request.GET.get("todos", None)
    if todos is not None:
        asesores = Asesor.objects.all()
    elif city is None or city == "":
        asesores = Asesor.objects.all()
    else:
        asesores = Asesor.objects.filter(sucursal__city=city)
    return render(request, "asesores.html", {"asesores": asesores, "ciudades": ciudad})

def createasesor(request):
    citys = Sucursal.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        city = request.POST['sucursal']
        sucursal = Sucursal.objects.get(city=city)
        create = Asesor(name=name, sucursal=sucursal)
        create.save()
        return redirect("asesores")
    return render(request, 'createasesor.html', {"citys": citys})


def sucursales(request):
    citys = Sucursal.objects.all()
    return render(request, "sucursales.html", {"citys": citys})

def createsucursal(request):
    if request.method == "POST":
        city = request.POST['sucursal']
        sucursal, created = Sucursal.objects.get_or_create(city=city)
        if created:
            sucursal.save()
        return redirect("sucursales")
    return render(request, "createsucursal.html")

