from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("products/", views.products, name = "products"),
    path("search/", views.search, name = "search"),
    path("products/<int:pk>/", views.product_page, name = "product_detail")
]