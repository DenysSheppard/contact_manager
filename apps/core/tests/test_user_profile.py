from django.test import TestCase
from apps.core.models import UserProfile

class UserProfileModelTests(TestCase):
    def setUp(self):
        self.obj = UserProfile.objects.create(
            username="denys",
            full_name="Denys Sheppard",
            timezone="Europe/Kyiv",
            locale="uk",
        )

    def test_create_user_profile(self):
        self.assertEqual(self.obj.username, "denys")
        self.assertEqual(self.obj.locale, "uk")
        self.assertIn("Denys", self.obj.full_name)
