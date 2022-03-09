from django.contrib import admin

from stellaris.models import Category
from .models import Category, Gallery, Product
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Gallery)