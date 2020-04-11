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
from django.contrib import admin
from django.urls import path

from vacancy.views import MainView
from vacancy.views import VacancyView
from vacancy.views import CompanyView
from vacancy.views import CompanySingleVacancy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='Main_page_index'),
    path('vacancy/<str:code>/', VacancyView.as_view(), name='Speciality_page'),
    path('company/<str:name>/', CompanyView.as_view(), name='Companies_page'),
    path('company/<str:name>/<int:id>/', CompanySingleVacancy.as_view(), name='Company_single_vac')
]
