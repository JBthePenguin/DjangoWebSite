from django.contrib import admin
from websiteapp.models import (
    Page, FooterItem, SocialLink, CardButton, AlertMessage, FormPlaceHolder)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    search_fields = ('link_name', 'title_en', 'title_fr',)
    list_display = (
        'link_name', 'title_en', 'title_fr',
        'subtitle_en', 'subtitle_fr', 'position')


@admin.register(FooterItem)
class FooterItemAdmin(admin.ModelAdmin):
    search_fields = ('name_en', 'name_fr', 'position')
    list_display = ('name_en', 'name_fr', 'position')


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name', 'url', 'position')


@admin.register(CardButton)
class CardButtonAdmin(admin.ModelAdmin):
    search_fields = ('card_name', 'text_en', 'text_fr', 'position')
    list_display = ('card_name', 'text_en', 'text_fr', 'position')


@admin.register(AlertMessage)
class AlertMessageAdmin(admin.ModelAdmin):
    search_fields = ('name', 'text_en', 'text_fr')
    list_display = ('name', 'text_en', 'text_fr')


@admin.register(FormPlaceHolder)
class FormPlaceHolderAdmin(admin.ModelAdmin):
    search_fields = ('form_name', 'input_name')
    list_display = (
        'form_name', 'input_name', 'text_en', 'text_fr', 'position')
