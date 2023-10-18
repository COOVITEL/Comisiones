from django.db import models


class Cdats(models.Model):
    """"""
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    type = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"CDATS Desde {self.since} Hasta {self.until}"
