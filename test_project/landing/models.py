from django.db import models

class Subscriber(models.Model):
    email = models.EmailField()
    name = models.CharField("имя", max_length=120)

    def __str__(self):
        return self.email


    class Meta:
        verbose_name = 'Подписчик'
        verbose_name_plural = 'Подписчики'