from django.shortcuts import render
from django.views import View

from .models import Speciality, Company, Vacancy

# Create your views here.

class MainView(View):
    def get(self, request):

        specialities = Speciality.objects.all()[:8]
        companies = Company.objects.all()[:8]

        context = {
                   'specialities': specialities,
                   'companies': companies,
                   }

        return render(request, 'vacancy/index.html', context)


class AllVacalsyList(View):
    def get(self, request):
        vacancies = Vacancy.objects.all()
        count = len(Vacancy.objects.all())

        context = {
                    'vacancies': vacancies,
                    'count': count
                    }

        return render(request, 'vacancy/all_vacancies.html', context)


class SpecialityView(View):
    def get(self, request, code:str):

        response_data = Speciality.objects.get(code=code)
        vacancies1 = response_data.vacancies.all()

        context = {
                   'vacancies': vacancies1,
                   'count': len(response_data.vacancies.all()),
                   'name': code
                   }

        return render(request, 'vacancy/speciality.html', context)



class CompanyView(View):
    def get(self, request, name:str):

        response_data = Company.objects.get(name=name)
        vacancies2 = response_data.company_vacancies.all()

        context = {
                    'vacancies': vacancies2,
                    'count': len(response_data.company_vacancies.all()),
                    'name': name
                   }
        return render(request, 'vacancy/company.html', context)


class SpecialitySingleVacancy(View):
    def get(self, request, id:int):

        vacancies = Vacancy.objects.get(id=id)
        title = vacancies.title
        skills = vacancies.skills
        description = vacancies.description
        salary_min = vacancies.salary_min
        salary_max = vacancies.salary_max
        published_at = vacancies.published_at

        context = {
                    'title': title,
                    'skills': skills,
                    'description': description,
                    'salary_min': salary_min,
                    'salary_max': salary_max,
                    'published_at': published_at
                   }

        return render(request, 'vacancy/speciality_single_vacansy.html', context)
