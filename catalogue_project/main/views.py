from django.shortcuts import render, HttpResponse
from django.db.models import Q
from .models import Product

# Create your views here.
def home(request):
    """
    home page
    """
    return render(request, "home.html")

def products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        products = Product.objects.filter(Q(name__icontains=searched) |
                                          Q(category__name__icontains=searched) |
                                          Q(description__icontains=searched))
    else:
        searched = {}
        products = {}
    return render(request, "search_page.html", {"searched" : searched,
                                                "products" : products})