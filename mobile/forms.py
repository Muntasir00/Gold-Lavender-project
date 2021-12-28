from .models import Mobile
from django import forms
from django.forms import ModelForm
class MobileForm(ModelForm):
    class Meta():
        model = Mobile
        fields = ['brand_name', 'model_name', 'color', 'jan_code', 'image']