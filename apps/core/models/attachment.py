from django.db import models

class Attachment(models.Model):
    contact = models.ForeignKey('core.Contact', on_delete=models.CASCADE)
    file_name = models.CharField(max_length=200)
    file_url = models.URLField(blank=True)  # згодом можна FileField
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_name
