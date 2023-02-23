from django.contrib import admin
from product import models

# Register your models here.


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['category','name','description','price', 'discount_price', 'image']

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']