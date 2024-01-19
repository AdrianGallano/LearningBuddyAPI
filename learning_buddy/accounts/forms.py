from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "password"]
        widgets = {
            "password": forms.PasswordInput(attrs={"minlength":8}),
        }