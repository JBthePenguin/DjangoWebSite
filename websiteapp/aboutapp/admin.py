from django.contrib import admin
from websiteapp.aboutapp.models import Service, Skill


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    search_fields = ('name_en', 'name_fr',)
    list_display = ('name_en', 'name_fr',)


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    search_fields = ('name_en', 'name_fr',)
    list_display = ('name_en', 'name_fr',)
