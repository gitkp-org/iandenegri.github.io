from django.shortcuts import render
from .models import Social, WebsiteSection, Project, Interest

# Create your views here.

def home(request):
    interests = Interest.objects.all()
    context = {
        "interests": interests
    }
    return render(request, "website/home.html", context=context)