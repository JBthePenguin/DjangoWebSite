from django.shortcuts import render
from websitedjango import settings
from websiteapp.portfolioapp.models import PortfolioCategory, Project


def portfolio(request):
    """ return the portfolio page """
    categories = PortfolioCategory.objects.all()
    projects = Project.objects.all().order_by("date").reverse()
    context = {
        "portfolio": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
        "categories": categories,
        "projects": projects,
    }
    return render(request, 'portfolioapp/portfolio.html', context)


def project(request, project_id):
    """ return the page with the project selected """
    project = Project.objects.get(id=project_id)
    context = {
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
        "project": project,
    }
    return render(request, 'portfolioapp/project.html', context)
