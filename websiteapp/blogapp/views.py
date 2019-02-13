from django.shortcuts import render
from websitedjango import settings


def blog(request):
    """ return the index page """
    context = {
        "blog": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
    }
    return render(request, 'blogapp/blog.html', context)
