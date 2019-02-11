from django.shortcuts import render


def index(request):
    # index view
    context = {"index": "active"}
    return render(request, 'websiteapp/index.html', context)


def mentions(request):
    """ return the page with legal mentions"""
    return render(request, 'websiteapp/mentions.html')
