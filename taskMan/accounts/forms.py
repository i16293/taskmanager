from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    AuthenticationForm
)


    #ログインフォーム
class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label




User = get_user_model()

"""アカウント登録フォーム"""
class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
             'icon',
            'username', 'email',
            'password1', 'password2',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



""" アカウント更新フォーム """
class AccountsUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = (
            'icon',
            'username', 'email',
            'last_name', 'first_name',
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


