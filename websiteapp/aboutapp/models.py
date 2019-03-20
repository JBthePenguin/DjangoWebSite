from django.db import models
from django.db.models import F
from websitedjango import settings


# Category
class AboutCategory(models.Model):
    link_name = models.CharField(db_index=True, max_length=255, unique=True)
    name_en = models.CharField(db_index=True, max_length=255)
    name_fr = models.CharField(db_index=True, max_length=255)
    position = models.IntegerField(db_index=True, default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


def get_about_categories():
    """ return all categories in the good language """
    return AboutCategory.objects.values('link_name').annotate(
        name=F('name_{}'.format(settings.LANGUAGE_CODE))).order_by('position')


# Term
class Term(models.Model):
    category = models.ForeignKey(
        AboutCategory, db_index=True, default='', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to='about', default='')
    name_en = models.CharField(db_index=True, max_length=255)
    name_fr = models.CharField(db_index=True, max_length=255)
    description_en = models.TextField()
    description_fr = models.TextField()
    position = models.IntegerField(default=0)


def get_terms():
    """ return all terms in the good language """
    return Term.objects.annotate(
        name=F('name_{}'.format(settings.LANGUAGE_CODE)),
        description=F('description_{}'.format(
            settings.LANGUAGE_CODE))).all().order_by('position')
