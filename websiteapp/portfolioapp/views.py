from django.shortcuts import render
from websitedjango import settings


def portfolio(request):
    """ return the index page """
    context = {
        "portfolio": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
    }
    return render(request, 'portfolioapp/portfolio.html', context)
