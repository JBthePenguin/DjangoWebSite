from django.shortcuts import render
from websitedjango import settings


def contact(request):
    """ return the index page """
    context = {
        "contact": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
    }
    return render(request, 'contactapp/contact.html', context)
