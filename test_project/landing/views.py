from django.shortcuts import render
from . forms import SubscriberForm
from products.models import *

# def landing(request):
#     form = SubscriberForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         new_form = form.save()

#     return render(request, 'landing/landing.html', {'form' : form})

def home(request):
    products_images = ProductImg.objects.filter(is_active=True, is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1, is_active=True)
    products_images_laptops = products_images.filter(product__category__id=3, is_active=True)
    return render(request, 'landing/home.html', locals())