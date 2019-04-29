from django.shortcuts import render

# Create your views here.

def home(request):
    context = {
        "N/A": "N/A"
    }
    return render(request, "website/home.html", context=context)