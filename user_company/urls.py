from django.urls import path

from .views import LoginToResume, Resume_ask, Resume_Create, Resume_Edit

urlpatterns = [
               path('login/', LoginToResume.as_view()),
               path('', Resume_ask, name='resume_ask'),
               path('create/', Resume_Create, name='resume_create'),
               path('update/', Resume_Edit, name='resume_edit'),
              ]
