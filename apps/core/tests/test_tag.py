from django.test import TestCase
from apps.core.models import Tag

class TagModelTests(TestCase):
    def setUp(self):
        self.obj = Tag.objects.create(name="Important")

    def test_create_tag(self):
        self.assertEqual(self.obj.name, "Important")
