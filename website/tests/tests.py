# Django
from django.core.exceptions import (
    ObjectDoesNotExist,
    MultipleObjectsReturned,
)
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

# Local
from website.views import WebsiteUtility
from website.models import Social, WebsiteSection, Project, Interest, Owner

fake_file = SimpleUploadedFile(name='test_image.docx', content=open('website/tests/test_document.docx', 'rb').read())

# Create your tests here.
class TestWebsiteModels(TestCase):
    def setUp(self):
        self.Owner = Owner.objects.create(
            first_name = "Test",
            last_name = "Case",
            resume = fake_file
        )
    