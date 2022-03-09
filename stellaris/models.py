from distutils.command.upload import upload
from unicodedata import category
from django.db import models
from django.forms import FloatField

# Create your models here.


class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='images/category')
    description = models.TextField(max_length=500, null=False, blank=False)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to='images/foods')
    description = models.CharField(max_length=250, null=False, blank=False)
    price = models.FloatField(null=False,blank=False)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Gallery(models.Model):
    description = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='images/gallery')  
    date_taken = models.DateField(auto_now_add=False,auto_now=False)

    def __str__(self):
        return self.description
    
    class Meta:
        verbose_name_plural = "Gallery"
        get_latest_by = 'date_taken'

class PartyTraysCategory(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to='images/category')
    description = models.TextField(max_length=500, null=False, blank=False)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name

