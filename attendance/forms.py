from django.forms import ModelForm
from django import forms
from bootstrap_datepicker.widgets import DatePicker
from .models import HaribhaktDetail,KaryakarGroup


class HaribhaktDetailForm(ModelForm):

    class Meta:
        model = HaribhaktDetail
        fields = ['baps_type','name','mobile_no','address','user']

class KaryakarGroupForm(ModelForm):
    # karyakar_from = forms.DateField(
    #       widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True}))
    # karyakar_to = forms.DateField(
    #       widget=DatePicker(options={"format": "mm/dd/yyyy","autoclose": True}))
    class Meta:
        model = KaryakarGroup
        fields = ['group_id','karyakar','haribhakt','karyakar_from','karyakar_to','user']