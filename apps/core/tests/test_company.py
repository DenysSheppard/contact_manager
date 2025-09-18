from django.test import TestCase
from apps.core.models import Company

class CompanyModelTests(TestCase):
    def setUp(self):
        self.obj = Company.objects.create(
            name="TestCorp",
            industry="IT",
            website="https://testcorp.com"
        )

    def test_create_company(self):
        self.assertEqual(self.obj.name, "TestCorp")
        self.assertTrue(self.obj.website.startswith("https://"))
