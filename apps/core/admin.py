from django.contrib import admin
from .models import Contact, Company, Address, Tag, Interaction, Attachment, UserProfile

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone", "job_title", "created_at")
    search_fields = ("full_name", "email", "phone")
    list_filter = ("job_title",)

admin.site.register(Company)
admin.site.register(Address)
admin.site.register(Tag)
admin.site.register(Interaction)
admin.site.register(Attachment)
admin.site.register(UserProfile)
