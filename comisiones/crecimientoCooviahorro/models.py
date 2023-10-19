from django.db import models


class CrecimientoCooviahorro(models.Model):
    """"""
    since = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        """"""
        return f"Por cada {self.since}, comision de {self.value}"