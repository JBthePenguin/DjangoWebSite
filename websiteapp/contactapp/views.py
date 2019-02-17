from django.shortcuts import render
from django.core.mail import send_mail
from websitedjango import settings
from websiteapp.contactapp.forms import ContactForm


def contact(request):
    """ return the page with contact form
    save a message and send emai"""
    send_msg = False
    form = ContactForm(language=settings.LANGUAGE_CODE)
    if request.method == 'POST':
        # message has sent
        form = ContactForm(request.POST, language=settings.LANGUAGE_CODE)
        if form.is_valid():
            # save message in db
            message = form.save(commit=False)
            send_mail(
                message.subject,
                message.content,
                "".join([
                    "DjangoWebSite: ",
                    message.contact_name, " <- ",
                    message.contact_email, " -> "]),
                ['JBthePenguin'],
                fail_silently=False,
            )
            message.save()
            send_msg = True
            form = ContactForm(language=settings.LANGUAGE_CODE)
    context = {
        "contact": "active",
        "theme": settings.THEME,
        "language": settings.LANGUAGE_CODE,
        'form': form,
        'send_msg': send_msg,
    }
    return render(request, 'contactapp/contact.html', context)
