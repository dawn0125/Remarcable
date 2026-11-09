from django.shortcuts import render, HttpResponse
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
    return render(request, "search_page.html", {})