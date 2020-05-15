from django import forms
from django.contrib.auth.models import User

from .models import Resume
# from accounts.models import Profile


class ResumeForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    class Meta:
        model = Resume
        fields = '__all__'


class ResumeAskForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']
