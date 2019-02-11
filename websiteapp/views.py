from django.shortcuts import render


def index(request):
    # index view
    return render(request, 'websiteapp/index.html')
