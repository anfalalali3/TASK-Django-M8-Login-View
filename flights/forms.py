from django import forms
from django.contrib.auth import get_user_model


User = get_user_model()

class UserRegister(forms.ModelForm):
    class Mete:
        model = User
        fields = ["username","first_name","last_name","password"]
        widgets = {
            "password": forms.PasswordInput(),
        }


class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())