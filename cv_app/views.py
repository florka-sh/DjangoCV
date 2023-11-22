# cv_app/views.py

from django.shortcuts import render
from .models import Education, Experience, Skill

def cv(request):
    education = Education.objects.all()
    experience = Experience.objects.all()
    skills = Skill.objects.all()
    
    return render(request, 'cv_app/cv.html', {'education': education, 'experience': experience, 'skills': skills})
