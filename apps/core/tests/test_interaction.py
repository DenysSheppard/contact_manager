from django.test import TestCase
from apps.core.models import Interaction, Contact

class InteractionModelTests(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(full_name="Jane Doe", email="jane@example.com")
        self.obj = Interaction.objects.create(
            contact=self.contact,
            channel="email",
            subject="Greeting",
            notes="Hello!",
        )

    def test_create_interaction(self):
        self.assertEqual(self.obj.channel, "email")
        self.assertEqual(self.obj.subject, "Greeting")
        self.assertEqual(self.obj.contact.full_name, "Jane Doe")
