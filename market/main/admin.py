from django.contrib import admin

# Register your models here.
from main.models import Product, Category, Shop



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Shop)

