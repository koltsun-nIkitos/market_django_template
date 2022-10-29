from django.contrib import admin
from .models import *

class ProductImgInline(admin.TabularInline):
    """ Встроенная адмика изображений товара"""
    model = ProductImg
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    """ Админка товаров """
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImgInline]
    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImgAdmin(admin.ModelAdmin):
    """ Админка изображений к товару """
    list_display = [field.name for field in ProductImg._meta.fields]
    class Meta:
        model = ProductImg

admin.site.register(ProductImg, ProductImgAdmin)
