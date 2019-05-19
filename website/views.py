#DJANGO IMPORTS
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
#APP IMPORTS
from .models import Social, WebsiteSection, Project, Interest, Owner

# Create your views here.

def home(request):
    website_parts = build_website()
    owner = find_me("ian", "denegri")  # Ideally only you should be using this so you can just replace my first and last name with your own.
    context = {
        "interests": website_parts['interests'],
        "socials": website_parts['socials'],
        "sections": website_parts['sections'],
        "projects": website_parts['projects'],
        "owner": owner,
    }
    return render(request, "website/home.html", context=context)

def find_me(first_name, last_name, capitilize=True):
    """
    This function takes a first name and last name argument to look you up.
    This is mainly to make the project a little simpler and easier to use.
    EXAMPLE:
    print(find_me("ian", "denegri"))
    This will look through your Owner objects for "Ian" "Denegri"
    If you want to look for your first and last name in all lower case characters then set "capitilize" to False.
    EXAMPLE:
    print(find_me("ian", "denegri", capitilize=False))
    This will look through your Owner objects for "ian" "denegri"
    """
    if capitilize:
        first = str(first_name).capitalize()
    else:
        first = str(first_name)
    if capitilize:
        last = str(last_name).capitalize()
    else:
        last = str(last_name)
    try: 
        myself = Owner.objects.filter(first_name=first).filter(last_name=last).get()
        return myself
    except ObjectDoesNotExist:
        print("The user you're looking for doesn't exist! Did you enter your first and last name properly? \n\
If you did, then are you sure that you created your Owner object in the Owner model table?")

def build_website():
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