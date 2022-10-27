from django.contrib import admin
from .models import *

class ProductImgInline(admin.TabularInline):
    model = ProductImg
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Product._meta.fields]
    inlines = [ProductImgInline]

    class Meta:
        model = Product

admin.site.register(Product, ProductAdmin)

class ProductImgAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductImg._meta.fields]

    class Meta:
        model = ProductImg

admin.site.register(ProductImg, ProductImgAdmin)
