from django.contrib import admin
from .models import *

class ProductOrderInline(admin.TabularInline):
    """ Встроеная админка всех товаров в заказе """
    model = ProductOrder
    extra = 0

class StatusAdmin(admin.ModelAdmin):
    """ Адмика статусов заказа """
    list_display = [field.name for field in Status._meta.fields]
    class Meta:
        model = Status

admin.site.register(Status, StatusAdmin)

class OrderAdmin(admin.ModelAdmin):
    """ Адмика заказа """
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductOrderInline] # встроенная админка

    class Meta:
        model = Order

admin.site.register(Order, OrderAdmin)

class ProductOrderAdmin(admin.ModelAdmin):
    """ Админка  списка товаров в заказе """
    list_display = [field.name for field in ProductOrder._meta.fields]
    class Meta:
        model = ProductOrder

admin.site.register(ProductOrder, ProductOrderAdmin)

class ProductInBasketAdmin(admin.ModelAdmin):
    """ Админка  списка товаров в корзине """
    list_display = [field.name for field in ProductInBasket._meta.fields]
    class Meta:
        model = ProductInBasket

admin.site.register(ProductInBasket, ProductInBasketAdmin)