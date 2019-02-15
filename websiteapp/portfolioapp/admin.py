from django import forms
from django.contrib import admin
from websiteapp.portfolioapp.models import PortfolioCategory, Project


@admin.register(PortfolioCategory)
class PortfolioCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name_en', 'name_fr',)
    list_display = ('name_en', 'name_fr',)


class CustomModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s - %s" % (obj.name_en, obj.name_fr)


class ProjectAdminForm(forms.ModelForm):
    category = CustomModelChoiceField(queryset=PortfolioCategory.objects.all())

    class Meta:
        model = Project
        fields = "__all__"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    search_fields = (
        'title_en', 'title_fr', 'category__name_fr', 'category__name_en')
    list_display = ('title_en', 'title_fr', 'get_category')

    def get_category(self, obj):
        return "%s - %s" % (obj.category.name_en, obj.category.name_fr)

    get_category.admin_order_field = 'category'
    get_category.short_description = 'Category'
