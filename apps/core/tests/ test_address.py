from django.test import TestCase
from apps.core.models import Address

class AddressModelTests(TestCase):
    def test_create_address(self):
        obj = Address.objects.create(
            label="home",
            street="Khreshchatyk 10",
            city="Kyiv",
            postal_code="01001",
            country="Ukraine",
        )
        self.assertEqual(obj.city, "Kyiv")
        self.assertEqual(str(obj), "home, Kyiv")
