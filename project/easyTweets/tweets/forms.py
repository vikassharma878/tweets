from django import forms
from .models import tweets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class tweetForm(forms.ModelForm):
    class Meta:
        model = tweets
        fields = ['text','photo']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields =('username','email','password1','password2')