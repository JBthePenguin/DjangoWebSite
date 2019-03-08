from django.shortcuts import render
from websitedjango import settings
from websiteapp.views import Context
from websiteapp.portfolioapp.models import PortfolioCategory, Project


def update_lang_proj(project):
    """ update language for a project """
    if settings.LANGUAGE_CODE == "fr":
        project.title = project.title_fr
        project.subtitle = project.subtitle_fr
        project.description = project.description_fr
    else:
        project.title = project.title_en
        project.subtitle = project.subtitle_en
        project.description = project.description_en
    project.save(update_fields=["title", "subtitle", "description"])


def portfolio(request):
    """ return the portfolio page """
    context = Context()
    context.update(
        portfolio="text-danger",
        id="portfolio")
    # update language for title and button in card
    titles = [context["navbar_items"][1]]
    if settings.LANGUAGE_CODE == "fr":
        titles.append("La présentation des travaux.")
        btn_card_text = "Voir les détails"
    else:
        titles.append("The presentation of the works.")
        btn_card_text = "View details"
    context.update(
        titles=titles,
        btn_card_text=btn_card_text)
    # update language for list items and categories
    categories = PortfolioCategory.objects.all()
    list_items = []
    for category in categories:
        if settings.LANGUAGE_CODE == "fr":
            category.name = category.name_fr
        else:
            category.name = category.name_en
        category.save(update_fields=["name"])
        list_items.append(category.name)
    context.update(list_items=list_items, categories=categories)
    # update language for projects
    projects = Project.objects.all().order_by("date").reverse()
    for project in projects:
        update_lang_proj(project)
    context.update(projects=projects)
    return render(request, 'portfolioapp/portfolio.html', context)


def project(request, project_id):
    """ return the page with the project selected """
    context = Context()
    context.update(
        portfolio="text-danger",
        id="project")
    # update language for the project
    project = Project.objects.get(id=project_id)
    update_lang_proj(project)
    if settings.LANGUAGE_CODE == "fr":
        project.category.name = project.category.name_fr
        btn_site_text = "Site Web"
        btn_code_text = "Code Source"
    else:
        project.category.name = project.category.name_en
        btn_site_text = "Website"
        btn_code_text = "Source code"
    project.save(update_fields=["category"])
    titles = [
        project.category.name,
        project.title]
    context.update(
        titles=titles,
        btn_site_text=btn_site_text,
        btn_code_text=btn_code_text,
        project=project)
    return render(request, 'portfolioapp/project.html', context)
