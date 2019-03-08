from django.db import models


class PortfolioCategory(models.Model):
    name_en = models.CharField(db_index=True, max_length=255)
    name_fr = models.CharField(db_index=True, max_length=255)
    name = models.CharField(max_length=255, default='')


class Project(models.Model):
    category = models.ForeignKey(
        PortfolioCategory, db_index=True, default='', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio', default='')
    title_en = models.CharField(db_index=True, max_length=255)
    title_fr = models.CharField(db_index=True, max_length=255)
    title = models.CharField(max_length=255, default='')
    subtitle_en = models.CharField(db_index=True, max_length=255)
    subtitle_fr = models.CharField(db_index=True, max_length=255)
    subtitle = models.CharField(max_length=255, default='')
    description_en = models.TextField()
    description_fr = models.TextField()
    description = models.TextField(default='')
    link = models.CharField(max_length=255, default='')
    github_link = models.CharField(max_length=255, default='')
    date = models.DateField()
