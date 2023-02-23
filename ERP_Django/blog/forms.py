from django import forms
from django.contrib.auth.models import User

from .models import Order, DayTask


class DayTaskForm(forms.ModelForm):
    order = forms.ModelChoiceField(queryset=Order.objects.all(), empty_label="(Nothing)")

    class Meta:
        model = DayTask
        fields = ['site', 'worker', 'serial_number', 'operation', 'time']


# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']
