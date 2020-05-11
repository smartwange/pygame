from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    '''username，password名称要和表单中的name保持一致'''
    username=forms.CharField(required=True,min_length=2)
    password=forms.CharField(required=True,min_length=3)



class CaptchaTestForm(forms.Form):
    captcha = CaptchaField()