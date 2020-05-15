from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.views import View

# from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from django.shortcuts import render

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

# from django.urls import reverse

from .models import Resume, Application
# from accounts.models import Profile

from .forms import ResumeForm, ResumeAskForm


class LoginToResume(View):
    login_url = 'login'

    def get(self, request):
        user = request.user if request.user.is_authenticated else None

        if Resume.objects.filter(user=request.user):
            return redirect('resume_edit')
        else:
            return redirect('resume_ask')



def Resume_ask(request):
    form = ResumeAskForm()

    return render(request, 'user_company/resume_has_or_not.html', context={'form': form})


def Resume_Create(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)

        if form.is_valid():
            resume = form.save(commit=False)
            resume.user = request.user
            resume.save()

            #'Ваш профиль был успешно создан!
            return redirect('resume_edit')
    else:
        new_resume = Resume.objects.create(user=request.user, education='', experience='')
        instance = new_resume
        form = ResumeForm(instance=instance)
        return render(request, 'user_company/resume_create.html', {'form': form})


def Resume_Edit(request):

    instance = Resume.objects.get(user=request.user)
    form = ResumeForm(request.POST, instance=instance)
    if request.method == 'POST':

        if form.is_valid():
            form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect('resume_edit')
        else:
            return render(request, 'user_company/resume_edit.html', {'form': form})

    else:
        form = ResumeForm(instance=instance)
        return render(request, 'user_company/resume_edit.html', {'form': form})
