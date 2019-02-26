from django.shortcuts import render
from websitedjango import settings
from websiteapp.aboutapp.models import Service, Skill


def about(request):
    """ return the about page """
    services = Service.objects.all()
    skills = Skill.objects.all()
    context = {
        "about": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
        "services": services,
        "skills": skills,
    }
    return render(request, 'aboutapp/about.html', context)
