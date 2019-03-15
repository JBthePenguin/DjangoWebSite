from django.shortcuts import render
from django.core.mail import send_mail
from websiteapp.context import Context
from websiteapp.models import get_page, get_buttons_card, get_alert_message
from websiteapp.blogapp.models import (
    get_blog_categories, get_all_posts, get_post, get_comments)
from websiteapp.blogapp.forms import CommentForm


def blog(request):
    """ return the blog page """
    # Page blog
    page = get_page("blog")
    # Categories
    categories = get_blog_categories()
    # Post
    posts = get_all_posts()
    # Card button
    buttons_card = get_buttons_card("blog")
    context = Context()
    context.update(
        page=page, categories=categories,
        posts=posts, btn_card_text=buttons_card[0].text)
    return render(request, 'blogapp/blog.html', context)


def post(request, post_name):
    """ return the page with the post selected """
    # Post
    post = get_post(post_name)
    # Page post
    page = {
        "link_name": "blog",
        "title": "Blog | {}".format(post.category_name),
        "subtitle": post.title}
    # Main titles
    main_titles = get_page("post")
    # Comments
    comments = get_comments(post_name)
    if len(comments) == 0:
        # Alert message
        no_comment = get_alert_message("no comment")
    else:
        no_comment = False
    # Card button
    buttons_card = get_buttons_card("comment")
    # Form POST
    form = CommentForm()
    add_comment = False
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # send a message to admin to inform him
            # that a comment has been added and save it in db
            comment = form.save(commit=False)
            comment.post = post
            send_mail(
                "A comment was added.",
                "'{}'\nhas been added to the post '{}' by {} <- {} ->".format(
                    comment.text, post_name,
                    comment.author_name, comment.author_email),
                "DjangoWebSite", ['JBthePenguin'], fail_silently=False)
            comment.save()
            form = CommentForm()
            # Alert message
            add_comment = get_alert_message("add comment")
    context = Context()
    context.update(
        page=page, main_titles=main_titles,
        btn_card_text=buttons_card[0].text, post=post,
        comments=comments, form=form,
        no_comment=no_comment, add_comment=add_comment)
    return render(request, 'blogapp/post.html', context)
