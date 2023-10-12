from django.db import models


class Colocaciones(models.Model):
    """"""
    tasaMin = models.CharField(max_length=50)
    tasaMax = models.CharField(max_length=50)
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.type} Colocaciones Desde {self.since} Hasta {self.until}"
