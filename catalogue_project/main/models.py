from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 200)

class Tags(models.Model):
    """
    
    """
    name = models.CharField(max_length = 200)

class Product(models.Model):
    name = models.CharField(max_length = 200)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    tags  = models.ManyToManyField(Tags)
