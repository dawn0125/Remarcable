from django.db import models

# Create your models here.

class Base(models.Model):
    name = models.CharField(max_length = 200)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
class Category(Base):
    """
    Broad categories for items found in a beauty store.
    Examples include hair, makeup, fragrance.
    """
    pass

class Tag(Base):
    """
    Specific tags for items found in a beauty store.
    Examples include colours, consistency, and brands.
    """
    pass

class Product(Base):
    description = models.TextField()
    price = models.DecimalField(max_digits = 6, decimal_places=2)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tags  = models.ManyToManyField(Tag)