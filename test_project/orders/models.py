from django.db import models
from products.models import Product

class Status(models.Model):
    name = models.CharField("статус", max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField("активен",default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Статус {0} ".format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    total_price = models.DecimalField("Общая стоимость", decimal_places=2, max_digits=10, default=0) #Цена всех товаров в заказе
    customer_name = models.CharField("имя", max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField("email", blank=True, null=True, default=None)
    customer_phone = models.CharField("телефон", max_length=48, blank=True, null=True, default=None)
    customer_adress = models.CharField("адрес", max_length=128, blank=True, null=True, default=None)
    commets = models.TextField("коментарий", blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='статус')
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Заказ {0} {1}".format(self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class ProductOrder(models.Model):
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="заказ")
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="товар")
    nmb = models.IntegerField("количество", default=1)
    price_per_item = models.DecimalField("цена товара",decimal_places=2, max_digits=10, default=0)
    total_price= models.DecimalField("общая стоимость",decimal_places=2, max_digits=10, default=0) #цена * количество
    is_active = models.BooleanField("активен", default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} ".format(self.product.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'