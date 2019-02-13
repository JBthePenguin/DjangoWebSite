from django.shortcuts import render, HttpResponse
from websitedjango import settings


def index(request):
    """ return the index page """
    context = {
        "index": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
    }
    return render(request, 'websiteapp/index.html', context)


def mentions(request):
    """ return the page with legal mentions"""
    context = {
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
    }
    return render(request, 'websiteapp/mentions.html', context)


def change_theme(request, theme):
    """ change the color of theme """
    settings.THEME = theme
    return HttpResponse("OK")


def change_lang(request, language):
    """ chnge the language """
    settings.LANGUAGE_CODE = language
    return HttpResponse("OK")
