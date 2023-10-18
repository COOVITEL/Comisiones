from django.db import models


class Cooviahorro(models.Model):
    """"""
    monto = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"Cooviahorro {self.value} por cada {self.monto}"
