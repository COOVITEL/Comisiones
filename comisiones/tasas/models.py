""""""
from django.db import models


class Afiliaciones(models.Model):
    """"""
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Afiliaciones Desde {self.since} Hasta {self.until}"


class Colocaciones(models.Model):
    """"""
    tasaMin = models.CharField(max_length=50)
    tasaMax = models.CharField(max_length=50)
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"Colocaciones Desde {self.since} Hasta {self.until}"

class Cdats(models.Model):
    """"""
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"CDATS Desde {self.since} Hasta {self.until}"


class Cooviahorro(models.Model):
    """"""
    monto = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Cooviahorro {self.value} por cada {self.monto}"


class AhorroVista(models.Model):
    """"""
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    porcentaje = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Ahorro Vista Desde {self.since} Hasta {self.until}"

class CrecimeintoBaseSocial(models.Model):
    """"""
    amount = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.value} por cada {self.amount}"

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