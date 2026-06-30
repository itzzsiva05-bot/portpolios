from django.shortcuts import render
from .models import Portfolio, Skill

def home(request):
    skills = Skill.objects.all()
    context = {
        'name': 'Siva',
        'skills': skills,
    }
    return render(request, 'home.html', context)

def portfolio(request):
    projects = Portfolio.objects.all().order_by('-created_at')
    return render(request, 'portfolio.html', {'projects': projects})



def fresher_resume(request):
    return render(request, 'fresher.html')

def experience_resume(request):
    return render(request, 'experience.html')