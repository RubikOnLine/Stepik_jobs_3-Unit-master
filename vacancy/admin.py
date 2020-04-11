from django.contrib import admin
from .models import Company, Speciality, Vacancy
# Register your models here.

@admin.register(Speciality)
class SpecialityAdmin(admin.ModelAdmin):
 list_display = ('code', 'id', 'title', 'picture')
 list_filter = ('code', 'title', 'id')
 search_fields = ('code', 'title')

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
 list_display = ('name', 'id', 'description')
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
