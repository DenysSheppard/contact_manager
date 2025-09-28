from django.contrib import admin
from django.urls import path, include
from apps.core import views
from apps.core.views import ContactDetailUpdateView
from django.contrib.auth import views as auth_views
from apps.core import views as core_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.welcome_view, name="welcome"),
    path("about/", views.about_view, name="about"),
    path("contacts/", views.contacts_list_view, name="contacts_list"),
    path("contacts/<int:pk>/", views.contact_detail_view, name="contact_detail"),
path("contacts/<int:pk>/edit/", views.contact_edit_view, name="contact_edit"),

    path("contacts/<int:pk>/edit/", ContactDetailUpdateView.as_view(), name="contact_edit"),
path("companies/", views.companies_view, name="companies"),
    path("addresses/", views.addresses_view, name="addresses"),
    path("tags/", views.tags_view, name="tags"),
path("accounts/login/",  auth_views.LoginView.as_view(
        template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="welcome"), name="logout"),
    path("admin/", admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
]
