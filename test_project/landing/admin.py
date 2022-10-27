from django.contrib import admin
from .models import Subscriber

class SubscriberAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
    #inlines = []
    #fields = []
    #exclude = ["email"]
    list_filter = ['email', 'name']
    search_fields = ['email', 'name']
    list_display_links = ["email"]
    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)

