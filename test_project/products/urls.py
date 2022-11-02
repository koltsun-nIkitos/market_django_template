from django.urls import path, include
from products import views

urlpatterns = [
    #path("/", include('landing.urls')),
    path('product/<int:product_id>/', views.product, name="product"), 
]