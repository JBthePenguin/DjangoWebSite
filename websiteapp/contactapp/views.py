from django.shortcuts import render
from django.core.mail import send_mail
from websitedjango import settings
from websiteapp.views import Context
from websiteapp.contactapp.forms import ContactForm


def contact(request):
    """ return the page with contact form
    save a message and send email"""
    context = Context()
    context.update(
        contact="text-danger",
        id="contact")
    # update language for title and send button
    titles = [context["navbar_items"][3]]
    if settings.LANGUAGE_CODE == "fr":
        titles.append("Nous contacter.")
        titles.append("Formulaire de contact")
        btn_message = "Envoyer"
        confirm_message = "Votre message a été envoyé."
    else:
        titles.append("Contact us.")
        titles.append("Contact form")
        btn_message = "Send"
        confirm_message = "Your message has been sent."
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
    context.update(
        titles=titles,
        btn_message=btn_message,
        confirm_message=confirm_message,
        form=form,
        send_msg=send_msg,
    )
    return render(request, 'contactapp/contact.html', context)
