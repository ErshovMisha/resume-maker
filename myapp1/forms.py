from django import forms
from django.forms import ModelForm
from myapp1.models import Res_Input
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TextInputForm(ModelForm):
    class Meta:
        model = Res_Input
        fields = ["name", 'second_name', "data"]


class ExampleForm(forms.Form):
    username = forms.CharField(label='Your name')
    password = forms.CharField(widget=forms.PasswordInput)

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user