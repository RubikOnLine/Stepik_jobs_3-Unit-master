from django.urls import path

from .views import UserResume

urlpatterns = [
               path('create/', UserResume.as_view()), name='resume_create'),
               path('edit/', EditResume.as_view()), name='resume_edit'),
]
