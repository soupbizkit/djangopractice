from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, "home.html", {})
    # return HttpResponse("<h1>Hello World</h1>") 

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def social_view(*args, **kwargs):
    return HttpResponse("<h2> Social page </h2>")