from django.db import models


class Service(models.Model):
    logo = models.ImageField(upload_to='about/service', default='')
    name_en = models.CharField(db_index=True, max_length=255)
    name_fr = models.CharField(db_index=True, max_length=255)
    name = models.CharField(max_length=255, default='')
    description_en = models.TextField()
    description_fr = models.TextField()
    description = models.TextField(default='')
    position = models.IntegerField(default=0)


class Skill(models.Model):
    logo = models.ImageField(upload_to='about/skill', default='')
    name_en = models.CharField(db_index=True, max_length=255)
    name_fr = models.CharField(db_index=True, max_length=255)
    name = models.CharField(max_length=255, default='')
    description_en = models.TextField()
    description_fr = models.TextField()
    description = models.TextField(default='')
    position = models.IntegerField(default=0)
