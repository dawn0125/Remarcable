"""
Dawn Zheng, Nov 2026
Filter class for products
"""
import django_filters
from . models import Product, Tag

class ProductFilter(django_filters.FilterSet):

    tags = django_filters.ModelMultipleChoiceFilter(queryset = Tag.objects.all())
    class Meta:
        model = Product
        fields = {"category" : ['exact']}