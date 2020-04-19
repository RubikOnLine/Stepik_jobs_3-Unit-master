from django.db import models

# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=15)
    surname = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    password = models.CharField(('password'), max_length=128)

    def __str__(self):
        return f'{self.id} {self.name} {self.company}'


class Application(models.Model):
    written_username = models.CharField(max_length=20)
    written_phone = models.CharField(max_length=16)
    written_cover_letter = models.TextField(blank=True)
    vacancy = models.ForeignKey('Vacancy', on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return f'{self.written_username}'


class Resume(models.Model):
    STATUS = [
                  ('dlf', 'Не ищу работу'),
                  ('ld', 'Рассматриваю предложения'),
                  ('lf', 'Ищу работу')
             ]

    GRADE = [
                  ('B', 'Стажер'),
                  ('J', 'Джуниор'),
                  ('M', 'Миддл'),
                  ('S', 'Синьор'),
                  ('L', 'Лид')
            ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='resume_user')
    status = models.CharField(max_length=3, choices=STATUS, default='dlf')
    salary = models.PositiveIntegerField(blank=True)
    specialty = models.ForeignKey('Speciality', on_delete=models.CASCADE, related_name='resume_speciality')
    grade = models.CharField(max_length=1, choices=GRADE, default='J')
    education = models.TextField(blank=True, verbose_name='Образование')
    experience = models.TextField(blank=True, verbose_name='Специализация')
    portfolio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} {self.user}'


class Speciality(models.Model):
    id = models.IntegerField(primary_key=True)
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    picture = models.ImageField(upload_to='MEDIA_SPECIALITY_IMAGE_DIR', height_field=None, width_field=None)

    def __str__(self):
        return f'{self.id} {self.code}'


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='MEDIA_COMPANY_IMAGE_DIR', height_field=None, width_field=None)
    description = models.TextField(blank=True)
    employee_count = models.IntegerField(blank=True)

    def __str__(self):
        return f'{self.name}'


class Vacancy(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=150)
    speciality = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='vacancies')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_vacancies')
    skills = models.TextField(blank=True)
    description = models.TextField(blank=True)
    salary_min = models.PositiveIntegerField(blank=True)
    salary_max = models.PositiveIntegerField(blank=True)
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
