from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from vacancy.models import Company, Speciality, Vacancy
from user_company.models import Application, Resume
# from accounts.models import Profile

# Register your models here.

# class ProfileInline(admin.StackedInline):
#     model = Profile
#     can_delete = False
#
#
# class UserAdmin(BaseUserAdmin):
#     inlines = [ProfileInline]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('written_username', 'written_phone', 'written_cover_letter', 'vacancy', 'user')
    list_filter = ('written_username', 'written_phone', 'written_cover_letter', 'vacancy', 'user')


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'surname', 'status', 'salary', 'spec', 'grade')
    list_filter = ('status', 'salary', 'spec', 'grade')


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
    list_display = ('title', 'speciality', 'company', 'skills')
    list_filter = ('title', 'speciality', 'company')
    search_fields = ('title', 'company')
    date_hierarchy = 'published_at'
    ordering = ('title', 'published_at')

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)
