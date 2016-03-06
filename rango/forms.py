from django import forms
from django.contrib.auth.models import User
from rango.models import *


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="category name")

    class Meta:
        model = Category
        fields = ('name',)


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="page title")
    url = forms.URLField(help_text="URL")

    class Meta:
        model = Page
        fields = ('title', 'url')

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     url = cleaned_data.get('url')
    #
    #     if url and (not url.startswith('http://') or not url.startswith('https://')):
    #         url = 'http://' + url
    #         cleaned_data['url'] = url
    #
    #     return cleaned_data


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password')
#
#
# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ('website', 'picture')
