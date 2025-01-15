from django import forms

class UserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    age = forms.IntegerField(label='Your age')
    email = forms.EmailField()
