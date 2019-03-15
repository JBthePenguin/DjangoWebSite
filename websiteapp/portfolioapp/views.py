from django.shortcuts import render
from websiteapp.context import Context
from websiteapp.models import get_page, get_buttons_card
from websiteapp.portfolioapp.models import (
    get_portfolio_categories, get_all_projects, get_project)


def portfolio(request):
    """ return the portfolio page """
    # Page portfolio
    page = get_page("portfolio")
    # Categories
    categories = get_portfolio_categories()
    # Projects
    projects = get_all_projects()
    # Card button
    buttons_card = get_buttons_card("portfolio")
    context = Context()
    context.update(
        page=page, categories=categories,
        projects=projects, btn_card_text=buttons_card[0].text)
    return render(request, 'portfolioapp/portfolio.html', context)


def project(request, project_name):
    """ return the page with the project selected """
    # Project
    project = get_project(project_name)
    # Page
    page = {
        "link_name": "portfolio",
        "title": "Portfolio | {}".format(project.category_name),
        "subtitle": project.title}
    # Card button
    buttons_card = get_buttons_card("project")
    context = Context()
    context.update(
        page=page,
        project=project,
        btn_card_text=buttons_card[0].text)
    return render(request, 'portfolioapp/project.html', context)
