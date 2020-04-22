from django.contrib import admin

from vacancy.models import Company, Speciality, Vacancy
from user_company.models import Application, Resume
from accounts.models import Profile

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('company',)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('written_username', 'written_phone', 'written_cover_letter', 'vacancy', 'user')
    list_filter = ('written_username', 'written_phone', 'written_cover_letter', 'vacancy', 'user')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'status', 'salary', 'specialty', 'grade')
    list_filter = ('user', 'status', 'salary', 'specialty', 'grade')


@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
 list_display = ('code', 'id', 'title', 'picture')
 list_filter = ('code', 'title', 'id')
 search_fields = ('code', 'title')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
 list_display = ('name', 'id', 'description', 'logo')
 list_filter = ('name', 'id', 'employee_count')



 @admin.register(Vacancy)
 class VacancyAdmin(admin.ModelAdmin):
  list_display = ('title', 'speciality', 'company', 'company_id', 'skills', 'salary_min', 'salary_max')
  list_filter = ('title', 'speciality', 'company', 'id')
  search_fields = ('title', 'company')
  # prepopulated_fields = {'slug': ('title',)}
  #raw_id_fields = ('title',)
  date_hierarchy = 'published_at'
  ordering = ('title', 'published_at')
