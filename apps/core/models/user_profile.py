from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=150, blank=True)
    timezone = models.CharField(max_length=50, blank=True)
    locale = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username
