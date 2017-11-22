from django import forms
from captcha.fields import CaptchaField

from .models import UserProfile


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(max_length=20, min_length=5, required=True)


class RegisterForm(forms.Form):
    username = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(max_length=20, min_length=5, required=True)
    password2 = forms.CharField(max_length=20, min_length=5, required=True)


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['image']


class UpdatePwdForm(forms.Form):
    password1 = forms.CharField(max_length=20, min_length=5, required=True)
    password2 = forms.CharField(max_length=20, min_length=5, required=True)


class UpdateUserInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'birthday', 'gender', 'address', 'mobile', 'email', ]


class UpdateEmailForm(forms.Form):
    email = forms.EmailField(required=True)