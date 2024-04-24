from django.contrib.auth.models import User
from django import forms

from .models import Post


class REGUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

        helptext = {
            'username': '',
            'email': '',
            'password': '',
        }
        labels = {
            'username': '',
            'email': '',
            'password': '',
        }
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),

        }

    # username =
    # email = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'User name'}))
    # password = forms.CharField(max_length=200,
    #                            widget=forms.TextInput(attrs={'placeholder': 'Password', 'type': 'password'}))


class AUTHUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


helptext = {
    'username': '',
    'password': '',
}
labels = {
    'username': '',
    'password': '',
}
widgets = {
    'username': forms.TextInput(attrs={'placeholder': 'Username'}),
    'password': forms.PasswordInput(attrs={'placeholder': 'Password'})
}


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = fields = ['title', 'content']
        helptext = {
            'title': '',
            'content': '',
        }
        labels = {
            'title': '',
            'content': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Title'}),
            'content': forms.TextInput(attrs={'placeholder': 'Content'}),

        }
