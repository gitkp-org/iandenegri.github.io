from django.shortcuts import render
from .models import Social, WebsiteSection, Project, Interest, Owner

# Create your views here.

def home(request):
    interests = Interest.objects.all()
    print(interests)
    socials = Social.objects.all()
    sections = WebsiteSection.objects.all()
    print(sections)
    projects = Project.objects.all()
    print(projects)
    owner = Owner.objects.filter(first_name="Ian").filter(last_name="Denegri")  # Ideally only you should be using this so you can just replace my first and last name with your own.
    print(owner)
    context = {
        "interests": interests,
        "socials": socials,
        "sections": sections,
        "projects": projects,
        "owner": owner,
    }
    return render(request, "website/home.html", context=context)