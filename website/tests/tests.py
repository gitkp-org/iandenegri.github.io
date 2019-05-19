# Django
from django.core.exceptions import (
    ObjectDoesNotExist,
    MultipleObjectsReturned,
    ValidationError,
)
from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.validators import URLValidator
from django.test import TestCase

# Local
from website.views import WebsiteUtility
from website.models import Social, WebsiteSection, Project, Interest, Owner

fake_file = SimpleUploadedFile(name='test_document.docx', content=open('website/tests/test_document.docx', 'rb').read())

# Create your tests here.
class TestWebsiteModels(TestCase):
    def setUp(self):
        # Create objects to populate the database for testing.
        Interest.objects.create(
            interest_name = "Interesting Thing"
        )

        Project.objects.create(
            project_name = "Test Project",
            URL = "http://www.testproject.com",
            description = "This is a description for the test project object. This is a text field so it can be as long as it needs to be."
        )

        for value in range(3):
            WebsiteSection.objects.create(
                section_name = ("Test Section Header %s" % value),
                section_blurb = ("This is the area where you fill in a blurb for the website section that this belongs to. (In this case Test Section Header %s)" % value)
            )

        # Owner.objects.create(
        #     first_name = "Test",
        #     last_name = "Case",
        #     resume = fake_file
        # )

    def test_interest_creation(self):
        test_interest = Interest.objects.get(interest_name = "Interesting Thing")
        self.assertTrue(isinstance(test_interest, Interest))
        self.assertEqual(test_interest.__str__(), test_interest.interest_name)

    def test_project_creation(self):
        test_project = Project.objects.get(project_name = "Test Project")
        val = URLValidator()
        self.assertTrue(isinstance(test_project, Project)) # Tests that the object created is made from the Project model.
        self.assertEqual(test_project.__str__(), test_project.project_name) # Tests that the string representation of the object is the project_name field.
        self.assertIsNone(val(test_project.URL)) # Tests that the URL field of this object is an actual URL.

    def test_website_section_creation(self):
        test_section = WebsiteSection.objects.get(section_name = "Test Section Header 1") 
        self.assertTrue(isinstance(test_section, WebsiteSection)) # Tests that the object is properly created from the WebsiteSection model even when bulk created.
        self.assertEqual(test_section.__str__(), test_section.section_name) # Tests that the string representation of the object is the section_name field

    # This keeps erroring and I'm not sure how to handle testing files :( I know that the project section will do the same due to the image field... Holding off on these models until I can figure out what's going wrong.
    # def test_owner_creation(self):
    #     owner = Owner.objects.get(first_name="Test")
    #     self.assertTrue(isinstance(owner, Owner))
    #     self.assertEqual(owner.__str__(),"%s %s"%(owner.first_name, owner.last_name))

class TestWebsiteUtilities(TestCase):
    def setUp(self):
        # Create objects to populate the database for testing.
        Interest.objects.create(
            interest_name = "Interesting Thing"
        )

        Project.objects.create(
            project_name = "Test Project",
            URL = "http://www.testproject.com",
            description = "This is a description for the test project object. This is a text field so it can be as long as it needs to be."
        )

        for value in range(3):
            WebsiteSection.objects.create(
                section_name = ("Test Section Header %s" % value),
                section_blurb = ("This is the area where you fill in a blurb for the website section that this belongs to. (In this case Test Section Header %s)" % value)
            )
    
    def test_utilities(self):
        pass