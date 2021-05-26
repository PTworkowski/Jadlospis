from django.conf import settings
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from account.models import Profile, MyUser

User = settings.AUTH_USER_MODEL

class CustomUserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = MyUser
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]


class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["address", "building", "apartment", "city", "zip_code", "profile_pic"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = MyUser
        fields = ["username", "first_name", "last_name", "email"]
