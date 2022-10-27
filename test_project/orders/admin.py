from django.contrib import admin
from .models import *

class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductOrderInline]

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class ProductOrderAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ProductOrder._meta.fields]

    class Meta:
        model = ProductOrder

admin.site.register(ProductOrder, ProductOrderAdmin)