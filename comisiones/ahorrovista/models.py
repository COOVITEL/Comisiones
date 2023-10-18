from django.db import models


class AhorroVista(models.Model):
    """"""
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    porcentaje = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Ahorro Vista Desde {self.since} Hasta {self.until}"
