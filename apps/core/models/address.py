from django.db import models

class Address(models.Model):
    label = models.CharField(max_length=80, blank=True)  # дім/робота тощо
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f"{self.label or 'address'}: {self.city}"
