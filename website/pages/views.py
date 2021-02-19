from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    my_context = {
        "bienvenida" : "whatsuppppp",
        "number": 2131354
    }
    return render(request, "home.html", my_context)
    # return HttpResponse("<h1>Hello World</h1>") 

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "this is about us",
        "my_number": 12345,
        "my_list" : [13,2456,3234,24,54,642]
    }
    return render(request, "about.html", my_context)

def social_view(*args, **kwargs):
    return HttpResponse("<h2> Social page </h2>")