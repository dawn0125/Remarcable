from .models import Category, Tag

def all_categories(request):
    """return a dictionary of all Category objects"""
    return {"all_categories" : Category.objects.all()}

def all_tags(request):
    """return a dictionary of all Tag objects"""
    return {"all_tags" : Tag.objects.all()}