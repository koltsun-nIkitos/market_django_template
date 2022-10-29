from pyexpat import model
from django import forms
from . models import Subscriber

class SubscriberForm(forms.ModelForm):
    """форма подписки"""
    class Meta:
        model = Subscriber
        exclude = [""]