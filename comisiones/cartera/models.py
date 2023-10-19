from django.db import models


class Cartera(models.Model):
    """ This class create a control to Crecimiento cartera productiva."""
    tasaMin = models.CharField(max_length=50)
    tasaMax = models.CharField(max_length=50)
    sinde = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self):
        """ Display class and object to call. """
        return f"Creciemiento Cartera, tasas {self.tasaMin} hasta {self.tasaMax}"