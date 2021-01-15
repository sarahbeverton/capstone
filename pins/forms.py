from django import forms
from .models import Comment


class PinForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 50%'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
    photo = forms.ImageField(required=False)
    url = forms.URLField(required=False)


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 2, 'cols': 50, 'placeholder': 'Add comment'}), label='Comment')

    class Meta:
        model = Comment
        fields = ['content']
        
