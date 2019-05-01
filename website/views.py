from django.shortcuts import render
from .models import Social, WebsiteSection, Project, Interest

# Create your views here.

def home(request):
    interests = Interest.objects.all()
    print(interests)
    socials = Social.objects.all()
    sections = WebsiteSection.objects.all()
    print(sections)
    projects = Project.objects.all()
    print(projects)
    context = {
        "interests": interests,
        "socials": socials,
        "sections": sections,
        "projects": projects
    }
    return render(request, "website/home.html", context=context)