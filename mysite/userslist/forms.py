from django import forms
from django.contrib.auth.models import User


class UserForm(forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    last_name = forms.CharField(label='Last name', max_length=100)
    age = forms.IntegerField(label='Your age', min_value=1, max_value=120)
    email = forms.EmailField()

