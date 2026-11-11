from django.shortcuts import render, HttpResponse, get_object_or_404
from django.db.models import Q
from .models import Product
from .filters import ProductFilter

# Create your views here.
def home(request):
    """home page"""
    products = Product.objects.all()

    # filter data if there is any applied
    productFilter = ProductFilter(request.GET, queryset = products)
    products = productFilter.qs

    return render(request, "home.html", {"products" : products})

def search(request):
    """search page"""
    if request.method == "GET":
        searched = request.GET['searched']
        # search product objects for if their name, category, tags,
        # or description contains the string searched
        # filter data if there is any applied
        products = Product.objects.filter(Q(name__icontains=searched) |
                                          Q(description__icontains=searched))
        
    else:
        searched = {}
        products = {}

    productFilter = ProductFilter(request.GET, queryset = products)
    products = productFilter.qs
    return render(request, "search_page.html", {"searched" : searched,
                                                "products" : products})

def product_page(request, pk):
    """page for displaying information about one product"""
    product = get_object_or_404(Product, pk=pk)
    return render(request, "product_page.html", {"product" : product})