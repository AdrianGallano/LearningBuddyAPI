from django import forms
from .models import User

class UserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=128)
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]
        widgets = {
            "password": forms.PasswordInput(attrs={"minlength":8}),
        }


class LoginForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), min_length=8, max_length=128)
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "password": forms.PasswordInput(attrs={"minlength":8}),
        }