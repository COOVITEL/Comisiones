from django.db import models


class Utilidad(models.Model):
    """"""
    rangoMin = models.CharField(max_length=50)
    rangoMax = models.CharField(max_length=50)
    small = models.CharField(max_length=50, null=True)
    medium = models.CharField(max_length=50, null=True)
    big = models.CharField(max_length=50, null=True)


    def __str__(self):
        """"""
        return f"Utilidad Oficina rango desde {self.rangoMin} hasta {self.rangoMax}"
