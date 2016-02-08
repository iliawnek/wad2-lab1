from django import forms
from rango.models import *


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="category name")
    # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="page title")
    url = forms.URLField(help_text="URL")
    # views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)
