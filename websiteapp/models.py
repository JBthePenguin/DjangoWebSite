from django.db import models
from django.db.models import F
from websitedjango import settings


# Page
class Page(models.Model):
    link_name = models.CharField(db_index=True, max_length=255, unique=True)
    title_fr = models.CharField(db_index=True, max_length=255)
    title_en = models.CharField(db_index=True, max_length=255)
    subtitle_fr = models.CharField(default='', max_length=255)
    subtitle_en = models.CharField(default='', max_length=255)
    position = models.IntegerField(db_index=True, default=0)


def get_navbar_items():
    """ return navbar items """
    return Page.objects.values('link_name').annotate(
        title=F('title_{}'.format(settings.LANGUAGE_CODE))).exclude(
            link_name__in=["post", "mentions", 'main-contact']).order_by(
                'position')


def get_all_page():
    """ return index, about, portfolio, blog and contact page
    using for main part in index """
    return Page.objects.annotate(
        title=F('title_{}'.format(settings.LANGUAGE_CODE)),
        subtitle=F('subtitle_{}'.format(
            settings.LANGUAGE_CODE))).all().exclude(link_name__in=[
                "post", "mentions", 'main-contact']).order_by('position')


def get_page(page_name):
    """ return one page with titles in the good langage """
    return Page.objects.annotate(
        title=F('title_{}'.format(settings.LANGUAGE_CODE)),
        subtitle=F('subtitle_{}'.format(settings.LANGUAGE_CODE))).get(
            link_name=page_name)


# Footer item
class FooterItem(models.Model):
    name_fr = models.CharField(db_index=True, max_length=255, unique=True)
    name_en = models.CharField(db_index=True, max_length=255, unique=True)
    position = models.IntegerField(db_index=True, default=0)


def get_footer_items():
    """  return all footer items in the good langage """
    return FooterItem.objects.annotate(
        name=F('name_{}'.format(settings.LANGUAGE_CODE))).order_by('position')


# Social link
class SocialLink(models.Model):
    name = models.CharField(db_index=True, max_length=255, unique=True)
    url = models.URLField(default='')
    position = models.IntegerField(db_index=True, default=0)


def get_social_links():
    """ return all social links """
    return SocialLink.objects.all().order_by('position')


# Card button
class CardButton(models.Model):
    card_name = models.CharField(db_index=True, max_length=255, default='')
    text_en = models.CharField(db_index=True, max_length=255)
    text_fr = models.CharField(db_index=True, max_length=255)
    position = models.IntegerField(db_index=True, default=0)


def get_buttons_card(card_name):
    """  return all buttons for one card in the good langage """
    return CardButton.objects.annotate(
        text=F('text_{}'.format(settings.LANGUAGE_CODE))).filter(
            card_name=card_name).order_by('position')


# Alert message
class AlertMessage(models.Model):
    name = models.CharField(db_index=True, max_length=255, unique=True)
    text_en = models.CharField(db_index=True, max_length=255, unique=True)
    text_fr = models.CharField(db_index=True, max_length=255, unique=True)


def get_alert_message(alert_name):
    """ return the message for one alert in the good langage """
    return AlertMessage.objects.annotate(text=F('text_{}'.format(
        settings.LANGUAGE_CODE))).get(name=alert_name)


# Form placeholder
class FormPlaceHolder(models.Model):
    form_name = models.CharField(db_index=True, max_length=255)
    input_name = models.CharField(db_index=True, max_length=255)
    text_en = models.CharField(max_length=255)
    text_fr = models.CharField(max_length=255)
    position = models.IntegerField(db_index=True, default=0)


def get_placeholders(form_name):
    """ return all placeholders for one form in good language """
    return FormPlaceHolder.objects.annotate(
        text=F('text_{}'.format(settings.LANGUAGE_CODE))).filter(
            form_name=form_name).order_by('position')
