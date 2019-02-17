from django import forms
from django.contrib import admin
from websiteapp.blogapp.models import BlogCategory, Post, Comment


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name_en', 'name_fr',)
    list_display = ('name_en', 'name_fr',)


class CategoryModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "%s - %s" % (obj.name_en, obj.name_fr)


class PostAdminForm(forms.ModelForm):
    category = CategoryModelChoiceField(queryset=BlogCategory.objects.all())

    class Meta:
        model = Post
        fields = "__all__"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    search_fields = (
        'title_en', 'title_fr', 'category__name_fr', 'category__name_en')
    list_display = ('title_en', 'title_fr', 'get_category', 'date')

    def get_category(self, obj):
        return "%s - %s" % (obj.category.name_en, obj.category.name_fr)

    get_category.admin_order_field = 'category'
    get_category.short_description = 'Category'


class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["valid"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    search_fields = (
        'author_name', 'author_email', 'post__title_fr',
        'post__title_en', 'valid')
    list_display = (
        'valid', 'get_post', 'author_name', 'author_email', 'date')

    def get_post(self, obj):
        return "%s - %s" % (obj.post.title_en, obj.post.title_fr)

    get_post.admin_order_field = 'post'
    get_post.short_description = 'Post'
