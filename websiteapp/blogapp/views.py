from django.shortcuts import render
from websitedjango import settings
from websiteapp.blogapp.models import BlogCategory, Post, Comment
from websiteapp.blogapp.forms import CommentForm


def blog(request):
    """ return the blog page """
    categories = BlogCategory.objects.all()
    posts = Post.objects.all().order_by("date").reverse()
    context = {
        "blog": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
        "categories": categories,
        "posts": posts,
    }
    return render(request, 'blogapp/blog.html', context)


def post(request, post_id):
    """ return the page with the project selected """
    post = Post.objects.get(id=post_id)
    form = CommentForm(language=settings.LANGUAGE_CODE)
    comment_saved = False
    if request.method == 'POST':
        # comment has sent
        form = CommentForm(request.POST, language=settings.LANGUAGE_CODE)
        if form.is_valid():
            # save comment in db
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            comment_saved = True
            form = CommentForm(language=settings.LANGUAGE_CODE)
    comments = Comment.objects.filter(
        post=post, valid=True).order_by("date").reverse()
    context = {
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
        "post": post,
        "comments": comments,
        "form": form,
        "comment_saved": comment_saved,
    }
    return render(request, 'blogapp/post.html', context)
