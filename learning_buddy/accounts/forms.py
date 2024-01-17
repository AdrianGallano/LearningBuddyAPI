from django import forms


class UserForm(forms.Form):
    first_name = forms.CharField(label="First name", max_length=50)
    last_name = forms.CharField(label="Last name", max_length=50)
    email = forms.EmailField(label="Email", max_length=50)
    password = forms.CharField(label="Password", widget=forms.PasswordInput, min_length=8)
