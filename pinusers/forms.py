from django import forms
from .models import PinUser


class UploadProfilePic(forms.ModelForm):
    profile_pic = forms.ImageField(required=False)

    class Meta:
        model = PinUser
        fields = ['profile_pic']
