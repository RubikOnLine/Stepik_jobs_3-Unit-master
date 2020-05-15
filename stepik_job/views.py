from django.shortcuts import redirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView

from django.views.generic import CreateView



class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class SignupView(CreateView):
   form_class = UserCreationForm
   template_name = 'signup.html'

   def get_success_url(self):
        return reverse('main_page')


def logout_view(request):
    logout(request)
    return redirect('/')
