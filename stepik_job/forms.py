from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class SignUpForm(UserCreationForm):
  company = forms.CharField()

  class Meta:
     model = User
     fields = ('username', 'company', 'password1', 'password2', )
