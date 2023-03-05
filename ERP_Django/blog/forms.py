from django import forms
from django.contrib.auth.models import User

from .models import Order, DayTask, ControlInput, SerialNumber


class DayTaskForm(forms.ModelForm):
    order = forms.ModelChoiceField(queryset=Order.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = DayTask
        fields = ['site', 'worker', 'serial_number', 'operation', 'time']


class ControlInputForm(forms.ModelForm):
    serial_number = forms.ModelChoiceField(queryset=SerialNumber.objects.none())

    class Meta:
        model = ControlInput
        fields = ['date_in', 'is_accepted_in', 'in_file']

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
