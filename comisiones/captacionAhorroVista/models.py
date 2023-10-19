from django.db import models


class CaptacionAhorroVista(models.Model):
    """"""
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        """"""
        return f"Saldo promedio ahorrovista desde {self.since} hasta {self.until}"
