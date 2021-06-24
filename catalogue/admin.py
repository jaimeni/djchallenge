from django.contrib import admin

# Register your models here.
from catalogue.models import Category, Product, ProductDetail


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'description']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['category', 'sku', 'name', 'description', 'pvp']


@admin.register(ProductDetail)
class ProductDetailAdmin(admin.ModelAdmin):
    fields = ['product', 'image']
