from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'style': 'width: 50%'}))
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'rows': 5}))
