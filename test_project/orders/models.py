from django.db import models
from products.models import Product
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Status(models.Model):
    """ Модель статуса """
    name = models.CharField("статус", max_length=24, blank=True, null=True, default=None)
    is_active = models.BooleanField("активен",default=True)
    
    created = models.DateTimeField("создан", auto_now_add=True)
    updated = models.DateTimeField("обновлен", auto_now=True)

    def __str__(self):
        return "Статус {0} ".format(self.name)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

class Order(models.Model):
    """ Модель заказа """
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    total_price = models.DecimalField("Общая стоимость", decimal_places=2, max_digits=10, default=0) #Цена всех товаров в заказе
    customer_name = models.CharField("имя", max_length=64, blank=True, null=True, default=None)
    customer_email = models.EmailField("email", blank=True, null=True, default=None)
    customer_phone = models.CharField("телефон", max_length=48, blank=True, null=True, default=None)
    customer_adress = models.CharField("адрес", max_length=128, blank=True, null=True, default=None)
    commets = models.TextField("коментарий", blank=True, null=True, default=None)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, verbose_name='статус')
    
    created = models.DateTimeField("создан", auto_now_add=True)
    updated = models.DateTimeField("обновлен",auto_now=True)

    def __str__(self):
        return "Заказ {0} {1}".format(self.id, self.status.name)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def save(self, *args, **kwargs):
        super(Order, self).save(*args, **kwargs)

class ProductOrder(models.Model):
    """ Модель товары в заказе """
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="заказ")
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="товар")
    nmb = models.IntegerField("количество", default=1)
    price_per_item = models.DecimalField("цена товара",decimal_places=2, max_digits=10, default=0)
    total_price= models.DecimalField("стоимость",decimal_places=2, max_digits=10, default=0) #цена * количество
    is_active = models.BooleanField("активен", default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{0} ".format(self.product.name)

    class Meta:
        verbose_name = 'Товар в заказе'
        verbose_name_plural = 'Товары в заказе'

    def save(self, *args, **kwargs):
        """ Переопределение метода save """
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = self.nmb * price_per_item

        super(ProductOrder, self).save(*args, **kwargs)


def product_in_order_post_save(sender, instance, created, **kwargs):
    """ функция для post_save - сохранение итоговой цены товаров; instance - то же что и self, но для модели"""
    order = instance.order
    all_products_in_order = ProductOrder.objects.filter(order=order, is_active=True)

    # Общая строимость
    order_total_price = 0
    for item in all_products_in_order:
        order_total_price += item.total_price

    instance.order.total_price = order_total_price
    instance.order.save(force_update=True) # обязательно не создание нового элемента, а обносление текущего!!!

# Соединение метода пост-сохранения для модели товары в заказе
post_save.connect(product_in_order_post_save, sender=ProductOrder)

class ProductInBasket(models.Model):
    """ Модель товары в корзине """
    session_key = models.CharField(max_length=128, blank=True, null=True, default=None)
    order = models.ForeignKey(Order, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="заказ")
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name="товар")
    nmb = models.IntegerField("количество", default=1)
    price_per_item = models.DecimalField("цена товара",decimal_places=2, max_digits=10, default=0)
    total_price= models.DecimalField("стоимость",decimal_places=2, max_digits=10, default=0) #цена * количество
    is_active = models.BooleanField("активен", default=True)
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "{0} ".format(self.product.name)

    class Meta:
        verbose_name = 'Товар в корзине'
        verbose_name_plural = 'Товары в корзине'

    def save(self, *args, **kwargs):
        """ Переопределение метода save """
        price_per_item = self.product.price
        self.price_per_item = price_per_item
        self.total_price = int(self.nmb) * price_per_item

        super(ProductInBasket, self).save(*args, **kwargs)