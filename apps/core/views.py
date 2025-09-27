from django.views import View
from django.shortcuts import render, get_object_or_404, redirect
from apps.core.models.contact import Contact
from apps.core.forms import ContactForm
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from django.contrib import messages
from django.views.generic import UpdateView
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from apps.core.forms import CompanyForm, AddressForm, TagForm

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
def welcome_view(request):
    return render(request, "core/pages/welcome.html")

def about_view(request):
    return render(request, "about.html")


def contacts_list_view(request):
    contacts = (
        Contact.objects
        .select_related('company')
        .all()
        .order_by('full_name')
    )
    return render(request, "core/pages/contacts_list.html", {"contacts": contacts})

def contact_detail_view(request, pk: int):
    contact = get_object_or_404(
        Contact.objects.select_related("company").prefetch_related("tags"),
        pk=pk,
    )
    return render(request, "core/pages/contact_detail.html", {"contact": contact})


class ContactDetailUpdateView(View):
    def get(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(instance=contact)
        return render(request, "core/pages/contact_detail.html", {"contact_form": form})

    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk)
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect("contact_detail", pk=pk)
        return render(request, "core/pages/contact_detail.html", {"contact_form": form})

    class ContactDetailUpdateView(UpdateView):
        model = Contact
        form_class = ContactForm
        template_name = "core/pages/contact_detail.html"
        success_url = reverse_lazy("contacts_list")

        class ContactDetailView(DetailView):
            model = Contact
            template_name = "core/pages/contact_detail.html"  # твій read-only шаблон
            context_object_name = "contact"

    class ContactDetailView(DetailView):
        model = Contact
        template_name = "core/pages/contact_detail.html"
        context_object_name = "contact"

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
        "objects": form._meta.model.objects.select_related(None).all(),
    })

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