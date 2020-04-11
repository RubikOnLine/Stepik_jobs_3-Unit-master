from django.shortcuts import render
from django.views import View

from .models import Speciality, Company, Vacancy

# Create your views here.

class MainView(View):
    def get(self, request):

        data_from_Specialities = Speciality.objects.all()[:8]
        data_from_Companies = Company.objects.all()[:8]

        context = {
                   'data_from_Specialities': data_from_Specialities,
                   'data_from_Companies': data_from_Companies,
                   }

        return render(request, 'vacancy/index.html', context)


class AllVacalsyList(View):
    def get(self, request):
        data_from_Vacancies = Vacancy.objects.all()
        count = Vacancy.objects.all().count()

        context = {
                    'data_from_Vacancies': data_from_Vacancies,
                    'count': count
                    }

        return render(request, 'vacancy/speciality.html', context)


class VacancyView(View):
    def get(self, request, code:str):

        s = Speciality.objects.get(code=code)
        data_from_Vacancies = s.vacancies.all()

        context = {
                   'data_from_Vacancies': data_from_Vacancies,
                   'count': s.vacancies.all().count(),
                   'name': code
                   }

        return render(request, 'vacancy/speciality.html', context)



class CompanyView(View):
    def get(self, request, name:str):

        s = Company.objects.get(name=name)
        data_from_Vacancies = s.company_vacancies.all()

        context = {
                    'data_from_Vacancies': data_from_Vacancies,
                    'count': s.company_vacancies.all().count(),
                    'name': name
                   }
        return render(request, 'vacancy/company.html', context)


class CompanySingleVacancy(View):
    def get(self, request, id:int):

        data_from_Vacancies = Vacancy.objects.get(id=id)

        context = {
                    'data_from_Vacancies': data_from_Vacancies,
                   }

        return render(request, 'vacancy/company_single_vacansy.html', context)
