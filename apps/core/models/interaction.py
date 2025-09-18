from django.db import models

class Interaction(models.Model):
    contact = models.ForeignKey('core.Contact', on_delete=models.CASCADE)
    channel = models.CharField(max_length=40, blank=True)  # call/email/meeting
    subject = models.CharField(max_length=200, blank=True)
    notes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject or f"Interaction with {self.contact.full_name}"
