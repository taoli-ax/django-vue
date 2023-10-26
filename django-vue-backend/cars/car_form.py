from django import forms

from cars.models import CarInfo


class CarInfoForm(forms.ModelForm):
    class Meta:
        model = CarInfo
        fields = ['name']