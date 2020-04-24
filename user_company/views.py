from django.shortcuts import render
from django.views import View

from .models import Resume, Application


class UserResume(View):

    def get(self, request, user):
        if request.user.is_authenticated:
            if user.profile.resume_user.all():
                return render(request, 'resume_edit.html')
            else:
                return render(request, 'resume_create.html')
