from django.urls import path
from resume import views

urlpatterns = [
    path('', views.home, name='home'),
    path('fresher-resume/', views.fresher_resume, name='fresher_resume'),
    path('experience-resume/', views.experience_resume, name='experience_resume'),
]