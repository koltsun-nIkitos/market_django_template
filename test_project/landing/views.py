from django.shortcuts import render


from . forms import SubscriberForm
from products.models import *

# def landing(request):
#     form = SubscriberForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         new_form = form.save()

#     return render(request, 'landing/landing.html', {'form' : form})

def home(request):
    products_images = ProductImg.objects.filter(is_active=True, is_main=True)
    return render(request, 'landing/home.html', locals())