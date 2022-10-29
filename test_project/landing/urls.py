from django.urls import path, re_path
from . import views



urlpatterns = [
    path("", views.home, name='home'), # переход на главную landing
] 

