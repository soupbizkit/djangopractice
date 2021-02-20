from django.shortcuts import render
from .models import Product
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.get(id=2)
    context={
        'object': obj
    }
    """context= {
        'title': obj.title,
        'description': obj.description
    }"""
    return render(request,"product/detail.html", context)