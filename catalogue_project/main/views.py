from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Q
from .models import Product

# Create your views here.
def home(request):
    """home page"""
    return render(request, "home.html")

def products(request):
    """page for displaying all products"""
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})

def search(request):
    """search page"""
    if request.method == "POST":
        searched = request.POST['searched']
        # search product objects for if their name, category, tags,
        # or description contains the string searched
        products = Product.objects.filter(Q(name__icontains=searched) |
                                          Q(category__name__icontains=searched) |
                                          Q(description__icontains=searched))
    else:
        searched = {}
        products = {}
    return render(request, "search_page.html", {"searched" : searched,
                                                "products" : products})

def product_page(request, pk):
    """page for displaying information about one product"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_page.html", {"product" : product})