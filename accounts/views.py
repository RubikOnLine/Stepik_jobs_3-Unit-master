from django.shortcuts import render, redirect

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
#from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView

from django.urls import reverse
#from .forms import SignUpForm


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'



class SignupView(CreateView):
   form_class = UserCreationForm
   template_name = 'signup.html'

   def get_success_url(self):
        return reverse('main_page')




# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             user.refresh_from_db()
#             user.profile.company = form.cleaned_data.get('company')
#             user.save()
#             my_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=my_password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = SignUpForm()
#         return render(request, 'signup.html', {'form': form})
