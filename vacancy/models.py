from django.db import models

# Create your models here.

class Speciality(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    picture = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.id} {self.code}'


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    logo = models.CharField(max_length=50)
    description = models.TextField(blank=True, db_index=True)
    employee_count = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_vacancies')
    skills = models.TextField(blank=True, db_index=True)
    description = models.TextField(blank=True, db_index=True)
    salary_min = models.PositiveIntegerField(blank=True)
    salary_max = models.PositiveIntegerField(blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} {self.company}'
