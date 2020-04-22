from django.db import models

from accounts.models import Profile
from vacancy.models import Speciality, Vacancy

# Create your models here.


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

    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='resume_user')
    status = models.CharField(max_length=3, choices=STATUS, default='dlf')
    salary = models.PositiveIntegerField(blank=True)
    specialty = models.ForeignKey(Speciality, on_delete=models.CASCADE, related_name='resume_speciality')
    grade = models.CharField(max_length=1, choices=GRADE, default='J')
    education = models.TextField(blank=True, verbose_name='Образование')
    experience = models.TextField(blank=True, verbose_name='Специализация')
    portfolio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.id} {self.user}'


class Application(models.Model):
    written_username = models.CharField(max_length=20)
    written_phone = models.CharField(max_length=16)
    written_cover_letter = models.TextField(blank=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='applications')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='applications')

    def __str__(self):
        return f'{self.written_username}'
