from django.forms import ModelForm
from django import forms
from .models import HaribhaktDetail,KaryakarGroup


class HaribhaktDetailForm(ModelForm):

    class Meta:
        model = HaribhaktDetail
        fields = ['baps_type','name','mobile_no','address','user']

class KaryakarGroupForm(ModelForm):

    class Meta:
        model = KaryakarGroup
        widgets = {
            'karyakar_from': forms.DateInput(attrs={'class': 'datepicker'}),
            'karyakar_to': forms.DateInput(attrs={'class': 'datepicker'}),
        }
        fields = ['group_id','karyakar','haribhakt','karyakar_from','karyakar_to','user']