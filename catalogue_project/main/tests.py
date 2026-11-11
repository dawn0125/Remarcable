from django.test import TestCase
from django.urls import reverse
from .models import Category, Tag, Product
# Create your tests here.

class SearchandFilterTests(TestCase):
    """test for search and filter"""
    @classmethod
    def setUpTestData(cls):
        cls.hair = Category.objects.create(name = "hair")
        cls.makeup = Category.objects.create(name = "makeup")
        cls.liquid = Tag.objects.create(name = "liquid")
        cls.brown = Tag.objects.create(name = "brown")

        cls.foundation = Product.objects.create(
            name = "Foundation",
            description = "Radiant Foundation",
            price = 60,
            category = cls.makeup
        )
        cls.foundation.tags.add(cls.liquid, cls.brown)
        cls.bronzer = Product.objects.create(
            name = "Bronzer",
            description = "radiant bronzing drops",
            price = 30,
            category = cls.makeup
        )
        cls.bronzer.tags.add(cls.brown)
        cls.hairoil = Product.objects.create(
            name = "Hair oil",
            description = "hair oil for hydration",
            price = 20,
            category = cls.hair
        )
        cls.hairoil.tags.add(cls.liquid)

    def get_products(self, url_name, **params):
        """helper function to get products"""

        # reverse dynamically generates url
        response = self.client.get(reverse(url_name), params)
        self.assertEqual(response.status_code, 200)
        return set(response.context["products"])
    
    def test_return_all(self):
        self.assertEqual(self.get_products("home"), {self.foundation, self.bronzer, self.hairoil})
    
    def test_filter_category(self):
        self.assertEqual(self.get_products("home", category = self.makeup.pk), {self.foundation, self.bronzer})

    def test_filter_tag(self):
        self.assertEqual(self.get_products("home", tags = [self.liquid.pk]), {self.foundation, self.hairoil})

    def test_search(self):
        self.assertEqual(self.get_products("search", searched = "hydration"), {self.hairoil})

    def test_combined(self):
        self.assertEqual(self.get_products("search", searched = "rad", tags = [self.liquid.pk]), {self.foundation})