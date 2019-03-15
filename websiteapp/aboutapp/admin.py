from django import forms
from django.contrib import admin
from websiteapp.aboutapp.models import AboutCategory, Term


@admin.register(AboutCategory)
class AboutCategoryAdmin(admin.ModelAdmin):
    search_fields = ('link_name', 'name_en', 'name_fr', 'position')
    list_display = ('link_name', 'name_en', 'name_fr', 'position')


class AboutCatModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s - %s" % (obj.name_en, obj.name_fr)


class TermAdminForm(forms.ModelForm):
    category = AboutCatModelChoiceField(queryset=AboutCategory.objects.all())

    class Meta:
        model = Term
        fields = "__all__"


@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    form = TermAdminForm
    search_fields = (
        'name_en', 'name_fr', 'category__name_fr', 'category__name_en')
    list_display = (
        'name_en', 'name_fr', 'get_category', 'logo',
        'description_en', 'description_fr', 'position')

    def get_category(self, obj):
        return "%s - %s" % (obj.category.name_en, obj.category.name_fr)

    get_category.admin_order_field = 'category'
    get_category.short_description = 'Category'
