from django.contrib.auth import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import LoginView, SignupView

from django.contrib.auth.views import LogoutView


urlpatterns = [
    # path('accounts/', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', SignupView.as_view(), name='signup')
]
