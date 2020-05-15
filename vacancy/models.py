from django.contrib.auth.models import User
from django.db import models

# from user_company.models import Application
# Create your models here.


class Speciality(models.Model):

    code = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='MEDIA_SPECIALITY_IMAGE_DIR', height_field=None, width_field=None)

    def __str__(self):
        return f'{self.id} {self.code}'


class Company(models.Model):

    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR', height_field=None, width_field=None)
    description = models.TextField(blank=True, null=True)
    employee_count = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):

    title = models.CharField(max_length=150)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='vacancy' )
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='vacancy')
    skills = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    salary_min = models.PositiveIntegerField(blank=True, null=True)
    salary_max = models.PositiveIntegerField(blank=True, null=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
