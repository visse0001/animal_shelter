from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import *


class AnimalForm(ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
