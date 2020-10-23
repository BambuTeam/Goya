"""user forms."""
# Django
from django import forms
# modelo
from django.contrib.auth.models import User
from users.models import Profile


class SigupForm(forms.Form):
    """Sign up form """
    username = forms.CharField(min_length=4, max_length=50, required=True)
    password = forms.CharField(max_length=70, widget=forms.PasswordInput())
    password_confirmation = forms.CharField(max_length=70, widget=forms.PasswordInput())
    first_name = forms.CharField(min_length=2, max_length=70)
    last_name = forms.CharField(min_length=2, max_length=50)
    email = forms.CharField(
        min_length=7,
        max_length=70,
        widget=forms.EmailInput()
    )

    def clean_username(self):
        """username must be unique"""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """verify password confimation """
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Password do not match.')
        return data

    def safe(self):
        """ create user and profile """
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()








