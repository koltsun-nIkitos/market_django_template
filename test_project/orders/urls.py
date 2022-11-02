from django.urls import path, include
from . import views


urlpatterns = [
    path("basket_adding/", views.basket_adding, name='basket_adding'),
]