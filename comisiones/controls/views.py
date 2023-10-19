from django.shortcuts import render, redirect
from .models import Asesor, Sucursal
from .read_excel import readExcel
import pandas as pd
import os

# Create your views here.

def welcome(request):
    """"""
    return render(request, "layout.html")

def asesores(request):
    """"""
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
    """"""
    citys = Sucursal.objects.all()
    if request.method == "POST":
        name = request.POST['name']
        city = request.POST['sucursal']
        sucursal = Sucursal.objects.get(city=city)
        create = Asesor(name=name, sucursal=sucursal)
        create.save()
        return redirect("asesores")
    return render(request, 'createasesor.html', {"citys": citys})

def deleteasesor(request, id):
    """"""
    asesor = Asesor.objects.get(id=id)
    asesor.delete()
    return redirect('asesores')


def sucursales(request):
    """"""
    citys = Sucursal.objects.all()
    return render(request, "sucursales.html", {"citys": citys})

def createsucursal(request):
    """"""
    if request.method == "POST":
        city = request.POST['city']
        create = Sucursal(city=city)
        create.save()
        return redirect("sucursales")
    return render(request, "createsucursal.html")

def deleteSucursal(request, id):
    """"""
    sucursal = Sucursal.objects.get(id=id)
    sucursal.delete()
    return redirect("sucursales")

def comisiones(request, name):
    """"""
    dates = {}
    dates = {"asesor": Asesor.objects.get(name=name),
             "afiliaciones": readExcel(name, "Afiliaciones", ["CD", "NOMBRES", "CODNOMINA", "NOMINA", "PROMOTOR", "F_CORTE", "SUBZONA", "SUCURSAL"]),
             #"colocaiones": readExcel(name, "Desembolsos", "NNPROMOT", ["A_OBLIGA", "CD", "NNASOCIA", "CODNOMINA", "NOMINA", "N_MODALI", "MONTO", "CARTERA", "NETO_ANTES", "P_TASEFEC", "NNPROMOT", "F_CORTE", "SUC_PRODUCTO"]),
             #"rotativo": readExcel(name, "Rotativos", ["A_NUMNIT", "N_NOMBRE", "CODNOMINA", "NOMINA", "N_MODALI", "A_OBLIGA", "SUMA_UTL", "F_CORTE", "SUC_PRODUCTO"]),
             #"cdat": readExcel(name, "CDAT", "PROMOTOR", ["CC", "NOMBRE_TERCERO", "A_TITULO", "Q_PLADIA", "V_TITULO", "M_ANTERIOR", "T_EFECTIVA", "PROMOTOR", "F_CORTE", "SUC_PRODUCTO"]),
             #"cooviahorro": readExcel(name, "Cooviahorro", "PROMOTOR", ["NNASOCIA", "CODNOMINA", "NUMERO", "SALDO", "PROMOTOR", "F_CORTE", "SUC_PRODUCTO"]),
             #"ahorro": readExcel(name, "Ah Vista", "PROMOTOR", ["CEDULA", "NNASOCIA", "CODNOMINA", "NOMINA", "CUENTA", "SALDO", "PROMOTOR", "F_CORTE", "SUC_PRODUCTO"])}
            }
    return render(request, "comisiones.html", dates)
