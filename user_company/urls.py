from django.urls import path

from .views import MyResumeView, Resume_Create, Resume_Edit

urlpatterns = [
               path('login/', MyResumeView.as_view()),
               path('create/', Resume_Create, name='resume_create'),
               path('edit/', Resume_Edit.as_view(), name='resume_edit'),
              ]
