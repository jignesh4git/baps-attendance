from django.forms import ModelForm
from django import forms
from .models import HaribhaktDetail


class HaribhaktDetailForm(ModelForm):

    class Meta:
        model = HaribhaktDetail
        fields = ['baps_type','name','mobile_no','address','user']
