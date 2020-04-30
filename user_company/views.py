from django.shortcuts import redirect

from django.views import View
# from django.views.decorators.http import require_http_methods
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.shortcuts import render

# from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# from django.urls import reverse

from .models import Resume, Application
from accounts.models import Profile

from .forms import ResumeEdit, ResumeCreate


class MyResumeView(View):
    login_url = 'login'

    def get(self, request):
        user = request.user if request.user.is_authenticated else None

        person = User.objects.get(username=request.user)
        has_resume = person.profile.resume_user.all().values()

        if has_resume:
            return redirect('resume_edit')
        else:
            return redirect('resume_create')


def Resume_Create(request):
    form = ResumeCreate()

    return render(request, 'user_company/resume_create.html', context={'form': form})


class Resume_Edit(View):
    def get(self, request):

        person = User.objects.get(username=request.user)
        has_resume = person.profile.resume_user.all().first()

        bound_form = ResumeEdit(instance=has_resume)

        name = person.first_name
        surname = person.last_name
        # context = {
        #            'data': has_resume,
        #            'name': name,
        #            'surname': surname,
        #            'form': newuser_form
        #             }

        return render(request, 'user_company/resume_edit.html', context={
                                                                         'form': bound_form,
                                                                         'name': name,
                                                                         'surname': surname
                                                                         })






# @require_http_methods(["GET", "POST"]) # Allow only GET, POST methods
# def Resume_Edit(request): #Add View in name for clarity
#     # GET request case
#     if request.method == "GET":
#         data = request.GET
#         person = User.objects.get(username=request.user)
#         has_resume = person.profile.resume_user.all().values()
#         if person:
#             name = person.first_name
#             surname = person.last_name
#             initial_data = {
#                                'data': has_resume,
#                                # 'name': person.first_name,
#                                # 'surname': person.last_name,
#                            }
#
#             form = ResumeEdit(initial=initial_data)
#
#     # POST request case
#     elif request.method == "POST":
#         form = ResumeEdit(request.POST)
#         # Assuming this works as intended
#         if form.is_valid():  # Check data
#             resume = form.save()
#             return HttpResponseRedirect(reverse('resume_edit', kwargs={'id': resume.id}))
#
#     context = {
#         "form" : form,
#         "person" : person,
#     }
#
#     return render(request, 'user_company/resume_edit.html', context)
