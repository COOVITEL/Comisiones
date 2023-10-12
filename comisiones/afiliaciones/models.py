from django.db import models


class Afiliaciones(models.Model):
    """
    This class create a structure to the afiliaciones comisions. 
    Since: From the number od affiliations that count towards commisioning.
    Until: Until the number of affiliations that count.
    Value: Value to pay for each comissiont.      
    """
    since = models.CharField(max_length=50)
    until = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

    def __str__(self) -> str:
        """String view of the admin"""
        return f"Afiliaciones desde {self.since} hasta {self.until}"
