from django.shortcuts import render
from websitedjango import settings


def about(request):
    """ return the index page """
    context = {
        "about": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
    }
    return render(request, 'aboutapp/about.html', context)
