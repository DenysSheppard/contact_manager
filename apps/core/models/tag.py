from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=20, blank=True)  # напр. #ff9900 або 'red'

    def __str__(self):
        return self.name
