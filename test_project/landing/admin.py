from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    """ Админка подписчиков """
    list_display = [field.name for field in Subscriber._meta.fields] # Показ полей
    #inlines = [] # встроеные админки в админку
    #fields = [] # поля
    #exclude = ["email"] #исключение полей
    list_filter = ['email', 'name'] # фильтры
    search_fields = ['email', 'name'] # поиск
    list_display_links = ["email"] # ссылки для перехода
    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)

