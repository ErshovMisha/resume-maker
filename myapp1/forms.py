from django import forms
from django.forms import ModelForm
from myapp1.models import Res_Input

class TextInputForm(ModelForm):
    class Meta:
        model = Res_Input
        fields = ["name", 'second_name', "data"]


class ExampleForm(forms.Form):
    name = forms.CharField(label='Your name')
    password = forms.CharField(label='Your password')