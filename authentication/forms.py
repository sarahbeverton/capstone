from django import forms
from pinusers.models import PinUser


class LoginForm(forms.Form):
    email = forms.EmailInput()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class SignUpForm(forms.ModelForm):
    class Meta:
        model = PinUser
        fields = (
            'email',
            'password',
            'username',
            'first_name',
            'last_name')
    widgets = {
        'email': forms.TextInput(),
        'password': forms.PasswordInput(),
        'username': forms.CharField(),
        'first_name': forms.CharField(),
        'last_name': forms.CharField()
    }
