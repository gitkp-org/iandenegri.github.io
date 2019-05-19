# Django
from django.core.exceptions import (
    ObjectDoesNotExist,
    MultipleObjectsReturned,
)
from django.test import TestCase

# Local
from .views import WebsiteUtility
from .models import Social, WebsiteSection, Project, Interest, Owner

# Create your tests here.
class TestWebsiteModels(TestCase):
    pass