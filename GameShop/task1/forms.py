from django import forms


class ContactForm(forms.Form):
    login = forms.CharField(max_length=30, label='Введите имя')
    password = forms.CharField(min_length=8, label='Введите пароль')
    repeat_password = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.IntegerField(max_value=999, label='Введите свой возраст')

