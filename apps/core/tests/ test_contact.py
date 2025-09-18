from django.test import TestCase
from apps.core.models import Contact, Company

class ContactModelTests(TestCase):
    def test_create_contact(self):
        company = Company.objects.create(name="TestCompany")
        obj = Contact.objects.create(
            first_name="Denys",
            last_name="Sheppard",
            email="denys@example.com",
            phone="123456789",
            company=company
        )
        self.assertEqual(obj.first_name, "Denys")
        self.assertEqual(str(obj), "Denys Sheppard")
