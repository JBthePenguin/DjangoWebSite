from django.db import models
from django.db.models import F
from websitedjango import settings


# Category
class PortfolioCategory(models.Model):
    link_name = models.CharField(db_index=True, default='', max_length=255)
    name_en = models.CharField(db_index=True, max_length=255)
    name_fr = models.CharField(db_index=True, max_length=255)
    position = models.IntegerField(db_index=True, default=0)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


def get_portfolio_categories():
    """ return all categories in the good language """
    return PortfolioCategory.objects.values('link_name').annotate(
        name=F('name_{}'.format(settings.LANGUAGE_CODE))).order_by('position')


# Project
class Project(models.Model):
    category = models.ForeignKey(
        PortfolioCategory, db_index=True, default='', on_delete=models.CASCADE)
    link_name = models.CharField(db_index=True, default='', max_length=255)
    image = models.ImageField(upload_to='portfolio', default='')
    title_en = models.CharField(db_index=True, max_length=255)
    title_fr = models.CharField(db_index=True, max_length=255)
    subtitle_en = models.CharField(max_length=255)
    subtitle_fr = models.CharField(max_length=255)
    description_en = models.TextField()
    description_fr = models.TextField()
    site_link = models.CharField(max_length=255, default='')
    date = models.DateField(db_index=True)


def get_all_projects():
    """ return all projects in the good language """
    return Project.objects.annotate(
        title=F('title_{}'.format(settings.LANGUAGE_CODE)),
        subtitle=F('subtitle_{}'.format(settings.LANGUAGE_CODE)),
        description=F('description_{}'.format(
            settings.LANGUAGE_CODE))).all().order_by('date').reverse()


def get_project(project_name):
    """ return a project in the good language """
    return Project.objects.annotate(
        title=F('title_{}'.format(settings.LANGUAGE_CODE)),
        subtitle=F('subtitle_{}'.format(settings.LANGUAGE_CODE)),
        description=F('description_{}'.format(settings.LANGUAGE_CODE)),
        category_name=F('category__name_{}'.format(
            settings.LANGUAGE_CODE))).get(link_name=project_name)
