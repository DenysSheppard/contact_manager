from django.shortcuts import render, get_object_or_404
from apps.core.models import Contact

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