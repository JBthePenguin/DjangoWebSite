from django.shortcuts import render, HttpResponse
from websitedjango import settings


def index(request):
    # index view
    context = {
        "index": "active",
        "theme": settings.THEME
    }
    return render(request, 'websiteapp/index.html', context)


def change_theme(request, theme):
    settings.THEME = theme
    return HttpResponse("OK")


def mentions(request):
    """ return the page with legal mentions"""
    context = {"theme": settings.THEME}
    return render(request, 'websiteapp/mentions.html', context)
