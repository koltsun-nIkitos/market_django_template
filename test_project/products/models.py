from django.db import models

class Product(models.Model):
    name = models.CharField("имя", max_length=64, blank=True, null=True, default=None)
    description = models.TextField("описание", blank=True, null=True, default=None)
    is_active = models.BooleanField("активен", default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "Товар {0} ".format(self.name)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'

class ProductImg(models.Model):
    product = models.ForeignKey(Product, blank=True, null=True, default=None, on_delete=models.CASCADE, verbose_name='изображение')
    image = models.ImageField("изображение",upload_to='product_images/')
    is_active = models.BooleanField("активен", default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{0} ".format(self.id)

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'