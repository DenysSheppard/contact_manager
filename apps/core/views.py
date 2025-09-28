from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.views import View
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView

from apps.core.models.contact import Contact
from apps.core.forms import ContactForm, CompanyForm, AddressForm, TagForm


# -------- Публічні сторінки --------
def welcome_view(request):
    return render(request, "core/pages/welcome.html")

def about_view(request):
    return render(request, "about.html")


# -------- Контакти (закриті) --------
@login_required
def contacts_list_view(request):
    contacts = (
        Contact.objects
        .select_related('company')
        .all()
        .order_by('full_name')
    )
    return render(request, "core/pages/contacts_list.html", {"contacts": contacts})

@login_required
def contact_detail_view(request, pk: int):
    contact = get_object_or_404(
        Contact.objects.select_related("company").prefetch_related("tags"),
        pk=pk,
    )
    return render(request, "core/pages/contact_detail.html", {"contact": contact})

@login_required
def contact_edit_view(request, pk):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, "Contact updated!")
            return redirect("contact_detail", pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, "core/pages/contact_edit.html", {"form": form, "contact": contact})


# Варіант редагування через класову в’юху (також закрито)
class ContactEditView(LoginRequiredMixin, UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = "core/pages/contact_edit.html"

    def get_success_url(self):
        return reverse("contact_detail", kwargs={"pk": self.object.pk})


# Якщо хочеш оновлення через кастомний View — теж закриваємо:
class ContactDetailUpdateView(LoginRequiredMixin, View):
    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(instance=contact)
        return render(request, "core/pages/contact_detail.html", {"contact_form": form, "contact": contact})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_detail", pk=pk)
        return render(request, "core/pages/contact_detail.html", {"contact_form": form, "contact": contact})


# Класові “read-only” в’юхи теж закриті:
class ContactListView(LoginRequiredMixin, ListView):
    model = Contact
    template_name = "core/pages/contacts_list.html"
    context_object_name = "contacts"

class ContactDetailView(LoginRequiredMixin, DetailView):
    model = Contact
    template_name = "core/pages/contact_detail.html"
    context_object_name = "contact"


# -------- Довідники (Companies / Addresses / Tags) — теж закриваємо --------
@login_required
@require_http_methods(["GET", "POST"])
def companies_view(request):
    if request.method == "POST":
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("companies")
    else:
        form = CompanyForm()
    return render(request, "core/pages/companies.html", {
        "title": "Companies",
        "form": form,
        "objects": form._meta.model.objects.all(),
    })

@login_required
@require_http_methods(["GET", "POST"])
def addresses_view(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addresses")
    else:
        form = AddressForm()
    return render(request, "core/pages/addresses.html", {
        "title": "Addresses",
        "form": form,
        "objects": form._meta.model.objects.all(),
    })

@login_required
@require_http_methods(["GET", "POST"])
def tags_view(request):
    if request.method == "POST":
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("tags")
    else:
        form = TagForm()
    return render(request, "core/pages/tags.html", {
        "title": "Tags",
        "form": form,
        "objects": form._meta.model.objects.all(),
    })
