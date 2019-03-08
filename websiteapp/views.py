from django.shortcuts import render, HttpResponse
from django.utils import translation
from websitedjango import settings


class Context(dict):
    """Default Context"""
    def __init__(self):
        """ settings for site's theme,
        language for title, navbar and footer """
        super(Context, self).__init__()
        # default
        self.update(
            bg_class="bg-{}".format(settings.THEME),
            navbar_class="navbar-{}".format(settings.THEME),
            btn_class="btn-{}".format(settings.THEME),
            lang="{}".format(settings.LANGUAGE_CODE),
            btn_theme="unchecked",
            btn_lang_style="dark")
        # update theme
        if settings.THEME == "dark":
            btn_theme = "checked"
            btn_lang_style = "light"
        else:
            btn_theme = "unchecked"
            btn_lang_style = "dark"
        # update language
        navbar_items = ["", "Portfolio", "Blog", "Contact"]
        if settings.LANGUAGE_CODE == "fr":
            title = "Titre du site"
            navbar_items[0] = "À propos"
            footer_items = [
                "Suivez-moi: ",
                "Thème: ",
                "Langue: ",
                "Mentions légales"]
            btn_lang = "checked"
        else:
            title = "Site's title"
            navbar_items[0] = "About"
            footer_items = [
                "Follow me:  ",
                "Theme: ",
                "Language: ",
                "Legal notices"]
            btn_lang = "unchecked"
        self.update(
            btn_theme=btn_theme,
            btn_lang_style=btn_lang_style,
            title=title,
            navbar_items=navbar_items,
            footer_items=footer_items,
            btn_lang=btn_lang)


def index(request):
    """ return the index page """
    context = Context()
    context.update(
        index="text-danger",
        id="index")
    if settings.LANGUAGE_CODE == "fr":
        titles = [
            "Titre du site",
            "La phrase d'accroche mettant en avant le service proposé."]
        main_texts = [
            "La description du responsable du site (entreprise, artisan, blogueur, ...).",
            "La présentation des travaux du responsable du site (entreprise, artisan, blogueur, ...).",
            "Le blog écrit par le responsable du site (entreprise, artisan, blogueur, ...).",
            "Le formulaire pour envoyer un message au responsable du site (entreprise, artisan, blogueur, ...)."]
    else:
        titles = [
            "Site's title",
            "The pickup line highlighting the proposed service."]
        main_texts = [
            "The description of the site's manager (company, freelancer, blogger, ...).",
            "The presentation of the works of the site's manager (company, freelancer, blogger, ...).",
            "The blog written by the site's manager (company, freelancer, blogger, ...).",
            "The form to send a message to the site's manager (company, freelancer, blogger, ...)."]
    context.update(
        titles=titles,
        main_texts=main_texts)
    return render(request, 'websiteapp/index.html', context)


def mentions(request):
    """ return the page with legal mentions"""
    # default french
    context = Context()
    context.update(
        index="text-danger",
        id="notices",
        titles=["Mentions légales.", ""],
        main_text="Ici les mentions.")
    if settings.LANGUAGE_CODE == "en":
        # update language
        context.update(
            titles=["Legal notices", ""],
            main_text="Here the notices")
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
