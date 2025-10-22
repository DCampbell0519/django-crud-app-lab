from django import forms
from .models import Thought
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['thought']

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']