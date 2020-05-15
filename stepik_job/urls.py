"""stepik_job URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from vacancy.views import MainView
from vacancy.views import AllVacalsyList
from vacancy.views import SpecialityView
from vacancy.views import CompanyView
from vacancy.views import SpecialitySingleVacancy

from .views import LoginView, logout_view, SignupView

import debug_toolbar


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main_page'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', logout_view, name='logout'),
    path('accounts/signup/', SignupView.as_view(), name='signup'),

    path('myresume/', include('user_company.urls')),
    # path('mycompany/', include('user_company.urls')),

    path('vacancies/', AllVacalsyList.as_view(), name='all_vacancies_list'),
    path('jobs/cat/<str:code>/', SpecialityView.as_view(), name='speciality_page'),
    path('companies/<str:name>/', CompanyView.as_view(), name='companies_page'),
    path('jobs/<int:id>/', SpecialitySingleVacancy.as_view(), name='speciality_single_page'),
    path('__debug__/', include(debug_toolbar.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
