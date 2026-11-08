from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    """
    home page
    """
    return render(request, "home.html")