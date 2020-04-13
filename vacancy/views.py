from django.shortcuts import render
from django.views import View

from .models import Speciality, Company, Vacancy

# Create your views here.

class MainView(View):
    def get(self, request):

        specialities = Speciality.objects.all()[:8]
        companies = Company.objects.all()[:8]

        # Для подсчета количества вакансий по той или иной специальности, и количества вакансий той или иной компании составляем словари следующего формата: count_dict_spec = {'frontend': количество} и count_dict_comp = {'назв. компании': количество}

        count_dict_spec = {spec.code: len(spec.vacancies.all()) for spec in specialities}
        count_dict_comp = {comp.name: len(comp.company_vacancies.all()) for comp in companies}

        context = {
                   'specialities': specialities,
                   'companies': companies,
                   'count_dict_spec': count_dict_spec,
                   'count_dict_comp': count_dict_comp
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
        vacancies = response_data.vacancies.all()

        context = {
                   'vacancies': vacancies,
                   'count': len(response_data.vacancies.all()),
                   'name': code
                   }

        return render(request, 'vacancy/speciality.html', context)



class CompanyView(View):
    def get(self, request, name:str):

        response_data = Company.objects.get(name=name)
        vacancies = response_data.company_vacancies.all()

        context = {
                    'vacancies': vacancies,
                    'count': len(response_data.company_vacancies.all()),
                    'name': name
                   }
        return render(request, 'vacancy/company.html', context)


class SpecialitySingleVacancy(View):
    def get(self, request, id:int):

        vacancies = Vacancy.objects.get(id=id)
        employee_c = vacancies.company.employee_count
        location = vacancies.company.location


        return render(request, 'vacancy/speciality_single_vacansy.html', {'vacancies': vacancies, 'count': employee_c, 'loc': location})
