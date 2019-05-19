#DJANGO IMPORTS
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
#APP IMPORTS
from .models import Social, WebsiteSection, Project, Interest, Owner

# Create your views here.

def home(request):
    website = WebsiteUtility("ian", "denegri")  # Ideally only you should be using this so you can just replace my first and last name with your own.
    website_parts = website.build_website()
    owner = website.find_me()

    context = {
        "interests": website_parts['interests'],
        "socials": website_parts['socials'],
        "sections": website_parts['sections'],
        "projects": website_parts['projects'],
        "owner": owner,
    }
    return render(request, "website/home.html", context=context)

class WebsiteUtility:
    """
    This class contains the functions that are used to build the data needed to populate the site.
    All you need to do is provide your first and last name. :-)
    """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def find_me(self, capitilize=True):
        """
        Finds you based on the first and last name you used when you instantiated the WebsiteUtility class.
        If your name needs to be not capitilized then please add "capitilize=False" to your find_me() arguments. :-)
        """
        if capitilize:
            first = str(self.first_name).capitalize()
        else:
            first = str(self.first_name)
        if capitilize:
            last = str(self.last_name).capitalize()
        else:
            last = str(self.last_name)
        try: 
            myself = Owner.objects.filter(first_name=first).filter(last_name=last).get()
            return myself
        except ObjectDoesNotExist:
            print("The user you're looking for doesn't exist! Did you enter your first and last name properly? \n\
                If you did then please make sure the capitilzation matches and if your name should be in lower case then please add 'capitilize=False' to the find_me() function as an argument. \
                Additionally, then are you sure that you created your Owner object in the Owner model table?")

    def build_website(self):
        """
        This function will build a dictionary that contains all the parts needed to build your website.
        This function assumes you have objects to display.
        """
        website_parts = dict()
        website_parts['interests'] = Interest.objects.all().order_by('pk')
        website_parts['socials'] = Social.objects.all().order_by('pk')
        website_parts['sections'] = WebsiteSection.objects.all().order_by('pk')
        website_parts['projects'] = Project.objects.all().order_by('pk')
        return website_parts
