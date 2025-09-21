from django.contrib import admin
from django.urls import path
from apps.core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.welcome_view, name="welcome"),
    path("about/", views.about_view, name="about"),
    path("contacts/", views.contacts_list_view, name="contacts_list"),
    path("contacts/<int:pk>/", views.contact_detail_view, name="contact_detail"),

]
