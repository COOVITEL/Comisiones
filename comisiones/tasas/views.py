from django.shortcuts import render


def comisiones(request):
    """
    This function create a render that conteion the
    diferents types of the comision.
    """
    return render(request, "types_comisiones.html")
