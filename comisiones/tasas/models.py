""""""
from django.db import models


class CrecimientoCartera(models.Model):
    """"""
    tasaMin = models.CharField(max_length=50)
    tasaMax = models.CharField(max_length=50)
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.value} x millon, tasa {self.tasaMin} - {self.tasaMax}, monto {self.since} - {self.until}"

class CrecimientoCdats(models.Model):
    """"""
    tasaMin = models.CharField(max_length=50)
    tasaMax = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.value} x millon, tasa entre {self.tasaMin} - {self.tasaMax}"

class CrecimientoCooviahorro(models.Model):
    """"""
    amount = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.value} x millon en crecimiento Cooviahorro"

class CaptacionAhorroVista(models.Model):
    """"""
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    porcentaje = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f""

class Utilidad(models.Model):
    """"""
    rangoSince = models.CharField(max_length=50)
    rangoUntil = models.CharField(max_length=50)
    size = models.CharField(max_length=50)
    value = models.CharField(max_length=50)