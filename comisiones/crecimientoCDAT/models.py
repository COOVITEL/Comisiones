from django.db import models


class CrecimientoCDAT(models.Model):
    """"""
    tasaMin = models.CharField(max_length=50)
    tasaMax = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        """"""
        return f"Crecimiento CDAT con tasa desde {self.tasaMin} hasta {self.tasaMax}"