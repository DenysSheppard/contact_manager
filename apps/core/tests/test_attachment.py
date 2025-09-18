from django.test import TestCase
from apps.core.models import Attachment, Contact

class AttachmentModelTests(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(full_name="Bob")
        self.obj = Attachment.objects.create(
            contact=self.contact,
            file_name="spec.pdf",
            file_url="https://example.com/spec.pdf",
            description="docs",
        )

    def test_create_attachment(self):
        self.assertEqual(self.obj.file_name, "spec.pdf")
        self.assertTrue(self.obj.file_url.endswith(".pdf"))
        self.assertEqual(self.obj.contact.full_name, "Bob")
