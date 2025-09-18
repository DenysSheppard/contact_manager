from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField(max_length=120, blank=True)
    phone = models.CharField(max_length=32, blank=True)
    job_title = models.CharField(max_length=120, blank=True)
    note = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # 🔹 Зв’язки
    company = models.ForeignKey('core.Company', on_delete=models.SET_NULL, null=True, blank=True)
    address = models.OneToOneField('core.Address', on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField('core.Tag', blank=True)

    def __str__(self):
        return self.full_name
