from django.db import models


class CrecimeintoBaseSocial(models.Model):
    """"""
    amount = models.CharField(max_length=50)
    value = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.value} por cada {self.amount}"