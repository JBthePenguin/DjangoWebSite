from django.db import models
from django.db.models import F
from websitedjango import settings


# Category
class BlogCategory(models.Model):
    link_name = models.CharField(max_length=255, default='')
    name_en = models.CharField(db_index=True, max_length=255)
    name_fr = models.CharField(db_index=True, max_length=255)
    position = models.IntegerField(db_index=True, default=0)


def get_blog_categories():
    """ return all categories in the good language """
    return BlogCategory.objects.values('link_name').annotate(
        name=F('name_{}'.format(settings.LANGUAGE_CODE))).order_by('position')


# Post
class Post(models.Model):
    category = models.ForeignKey(
        BlogCategory, db_index=True, default='', on_delete=models.CASCADE)
    link_name = models.CharField(db_index=True, default='', max_length=255)
    image = models.ImageField(upload_to='blog', default='')
    title_en = models.CharField(db_index=True, max_length=255)
    title_fr = models.CharField(db_index=True, max_length=255)
    content_en = models.TextField()
    content_fr = models.TextField()
    date = models.DateField(auto_now_add=True)


def get_all_posts():
    """ return all posts in the good language """
    return Post.objects.annotate(
        title=F('title_{}'.format(settings.LANGUAGE_CODE)),
        content=F('content_{}'.format(
            settings.LANGUAGE_CODE))).all().order_by('date').reverse()


def get_post(post_name):
    """ return a project in the good language """
    return Post.objects.annotate(
        title=F('title_{}'.format(settings.LANGUAGE_CODE)),
        content=F('content_{}'.format(settings.LANGUAGE_CODE)),
        category_name=F('category__name_{}'.format(
            settings.LANGUAGE_CODE))).get(link_name=post_name)


# Comment
class Comment(models.Model):
    post = models.ForeignKey(
        Post, db_index=True, default='', on_delete=models.CASCADE)
    author_name = models.CharField(db_index=True, max_length=255)
    author_email = models.EmailField(db_index=True, max_length=255)
    text = models.TextField()
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    valid = models.BooleanField(default=False)


def get_comments(post_name):
    """ return all comments for one post """
    return Comment.objects.filter(
        post__link_name=post_name, valid=True).order_by("date").reverse()
