from django.db import models

from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver

# from accounts.models import Profile
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

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='resumes')
    name = models.CharField(max_length=20, verbose_name='Имя')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    status = models.CharField(max_length=3, choices=STATUS, default='dlf', verbose_name='Готовность к работе', blank=True)
    salary = models.PositiveIntegerField(blank=True, null=True, verbose_name='Ожидаемое вознаграждение')
    spec = models.ForeignKey(Speciality, on_delete=models.CASCADE, default='2', related_name='resumes', verbose_name='Специализация', blank=True, null=True)
    grade = models.CharField(max_length=1, choices=GRADE, blank=True, default='J', verbose_name='Квалификация')
    education = models.TextField(blank=True, null=True, verbose_name='Образование')
    experience = models.TextField(blank=True, null=True, verbose_name='Опыт работы')
    portfolio = models.URLField(max_length=200, blank=True, verbose_name='Ссылка на портфолио')

# @receiver(post_save, sender=User)
# def create_user_resume(sender, instance, created, **kwargs):
#     if created:
#         Resume.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_resume(sender, instance, **kwargs):
#     instance.resumes.save()


    def __str__(self):
        return f'{self.user} {self.name} {self.surname}'



class Application(models.Model):
    written_username = models.CharField(max_length=20, blank=True)
    written_phone = models.CharField(max_length=16, blank=True)
    written_cover_letter = models.TextField(blank=True)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name="applications")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")

    def __str__(self):
        return f'{self.written_username}'
