from django import forms

class TextInputForm(forms.Form):
    text_input1 = forms.CharField(label="Ім'я", max_length=100)
    text_input2 = forms.CharField(label="Прізвище", max_length=100)
    text_input3 = forms.CharField(label="Дані", max_length=100)