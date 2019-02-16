from django.db import models


class BlogCategory(models.Model):
    name_en = models.CharField(db_index=True, max_length=255)
    name_fr = models.CharField(db_index=True, max_length=255)


class Post(models.Model):
    category = models.ForeignKey(
        BlogCategory, db_index=True, default='', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='blog', default='')
    title_en = models.CharField(db_index=True, max_length=255)
    title_fr = models.CharField(db_index=True, max_length=255)
    content_en = models.TextField()
    content_fr = models.TextField()
    date = models.DateField()


class Comment(models.Model):
    post = models.ForeignKey(
        Post, db_index=True, default='', on_delete=models.CASCADE)
    author_name = models.CharField(db_index=True, max_length=255)
    author_email = models.EmailField(db_index=True, max_length=255)
    text = models.TextField()
    date = models.DateTimeField(db_index=True, auto_now_add=True)
    valid = models.BooleanField(default=False)
