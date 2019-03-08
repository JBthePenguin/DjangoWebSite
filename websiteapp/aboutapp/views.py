from django.shortcuts import render
from websitedjango import settings
from websiteapp.views import Context
from websiteapp.aboutapp.models import Service, Skill


def about(request):
    """" return the about page """
    context = Context()
    context.update(
        about="text-danger",
        id="about")
    # update language for title and list items
    titles = [context["navbar_items"][0]]
    list_items = ["Services"]
    if settings.LANGUAGE_CODE == "fr":
        titles.append("La phrase décrivant le responsable du site (entreprise, artisan, blogueur, ...).")
        list_items.append("Compétences")
    else:
        titles.append("The sentence describing the site manager (company, freelancer, blogger, ...).")
        list_items.append("Skills")
    context.update(
        titles=titles,
        list_items=list_items)

    # update language for services and skills
    def update_language(model):
        """ update language for a model"""
        models = model.objects.all().order_by("position")
        for model in models:
            if settings.LANGUAGE_CODE == "fr":
                model.name = model.name_fr
                model.description = model.description_fr
            else:
                model.name = model.name_en
                model.description = model.description_en
            model.save(update_fields=["name", "description"])
        return models

    services = update_language(Service)
    skills = update_language(Skill)
    context.update(
        services=services,
        skills=skills)
    return render(request, 'aboutapp/about.html', context)
