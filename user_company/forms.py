from django import forms
from django.contrib.auth.models import User

from .models import Resume
from accounts.models import Profile


class ResumeEdit(forms.ModelForm):

    class Meta:
        model = Resume
        fields = ['status', 'salary', 'specialty', 'grade', 'education', 'experience', 'portfolio']
        name = forms.CharField(label='Имя')
        surname = forms.CharField(label='Фамилия')


class ResumeCreate(forms.ModelForm):

    class Meta:
        model = Profile

        fields = ['user']
