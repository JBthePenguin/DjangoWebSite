from django.shortcuts import render
from websiteapp.context import Context
from websiteapp.models import get_page
from websiteapp.aboutapp.models import get_about_categories, get_terms


def about(request):
    """" return the about page """
    # Page about
    page = get_page("about")
    # Categories
    categories = get_about_categories()
    # Terms
    terms = get_terms()
    context = Context()
    context.update(
        page=page,
        categories=categories,
        terms=terms)
    return render(request, 'aboutapp/about.html', context)
