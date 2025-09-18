from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=150)
    industry = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)
    city = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.name
