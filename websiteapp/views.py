from django.shortcuts import render, HttpResponse
from django.utils import translation
from websitedjango import settings
from websiteapp.models import get_all_page, get_page
from websiteapp.context import Context


def index(request):
    """ return the index page """
    pages = get_all_page()
    context = Context()
    context.update(page=pages[0], pages=pages[1:])
    return render(request, 'websiteapp/index.html', context)


def mentions(request):
    """ return the page with legal mentions"""
    page = get_page("mentions")
    context = Context()
    context.update(page=page)
    return render(request, 'websiteapp/mentions.html', context)


def change_theme(request, theme):
    """ change the color of theme """
    settings.THEME = theme
    return HttpResponse("ok")


def change_lang(request, language):
    """ change the language """
    settings.LANGUAGE_CODE = language
    translation.activate(settings.LANGUAGE_CODE)
    return HttpResponse("ok")
