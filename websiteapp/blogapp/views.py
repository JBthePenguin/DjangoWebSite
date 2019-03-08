from django.shortcuts import render
from websitedjango import settings
from websiteapp.views import Context
from websiteapp.blogapp.models import BlogCategory, Post, Comment
from websiteapp.blogapp.forms import CommentForm


def update_lang_post(post):
    """ update language for a post """
    if settings.LANGUAGE_CODE == "fr":
        post.title = post.title_fr
        post.content = post.content_fr
    else:
        post.title = post.title_en
        post.content = post.content_en
    post.save(update_fields=["title", "content"])


def blog(request):
    """ return the blog page """
    context = Context()
    context.update(
        blog="text-danger",
        id="blog")
    # update language for title and button in card
    titles = [context["navbar_items"][2]]
    if settings.LANGUAGE_CODE == "fr":
        titles.append("Les articles techniques.")
        btn_card_text = "Lire la suite"
    else:
        titles.append("The technical articles.")
        btn_card_text = "Read more"
    context.update(
        titles=titles,
        btn_card_text=btn_card_text)
    # update language for list items and categories
    categories = BlogCategory.objects.all()
    list_items = []
    for category in categories:
        if settings.LANGUAGE_CODE == "fr":
            category.name = category.name_fr
        else:
            category.name = category.name_en
        category.save(update_fields=["name"])
        list_items.append(category.name)
    context.update(list_items=list_items, categories=categories)
    # update language for posts
    posts = Post.objects.all().order_by("date").reverse()
    for post in posts:
        update_lang_post(post)
    context.update(posts=posts)
    return render(request, 'blogapp/blog.html', context)


def post(request, post_id):
    """ return the page with the post selected """
    context = Context()
    context.update(
        blog="text-danger",
        id="post")
    # update language for the post titles messages and btn send comment text
    post = Post.objects.get(id=post_id)
    update_lang_post(post)
    if settings.LANGUAGE_CODE == "fr":
        post.category.name = post.category.name_fr
        title_comment = "Commentaires"
        title_form = "Laisser un commentaire"
        messages = [
            "Votre commentaire sera ajouté dès que je l'aurai validé.",
            "Aucun commentaire pour cet article."]
        btn_comment = "Envoyer"
    else:
        post.category.name = post.category.name_en
        title_comment = "Comments"
        title_form = "Post a comment."
        messages = [
            "Your comment will be added as soon as I have validated it.",
            "No comment for this post."]

        btn_comment = "Send"
    post.save(update_fields=["category"])
    titles = [post.category.name, post.title, title_comment, title_form]
    # Form POST
    form = CommentForm(language=settings.LANGUAGE_CODE)
    comment_send = False
    if request.method == 'POST':
        # comment has sent
        form = CommentForm(request.POST, language=settings.LANGUAGE_CODE)
        if form.is_valid():
            # save comment in db
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            comment_send = True
            form = CommentForm(language=settings.LANGUAGE_CODE)
    # Comments
    comments = Comment.objects.filter(
        post=post, valid=True).order_by("date").reverse()
    context.update(
        titles=titles,
        btn_comment=btn_comment,
        post=post,
        comments=comments,
        form=form,
        comment_send=comment_send,
        messages=messages
    )
    return render(request, 'blogapp/post.html', context)
