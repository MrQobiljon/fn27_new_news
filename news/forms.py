from django import forms

from .models import Category


class PostForm(forms.Form):
    title = forms.CharField(max_length=250, widget=forms.TextInput(attrs={
        "placeholder": "Nomi",
        "class": "form-control"
    }), label='Nomi')
    content = forms.CharField(widget=forms.Textarea(attrs={
        "placeholder": "Matni",
        "class": "form-control"
    }), required=False)
    photo = forms.ImageField(widget=forms.FileInput(attrs={
        "class": "form-control"
    }))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), widget=forms.Select(attrs={
        "class": "form-select"
    }))
    published = forms.BooleanField(widget=forms.CheckboxInput(attrs={
        "class": "form-check-input",
        "checked": "checked"
    }))

