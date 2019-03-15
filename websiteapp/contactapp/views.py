from django.shortcuts import render
from django.core.mail import send_mail
from websiteapp.context import Context
from websiteapp.models import get_page, get_buttons_card, get_alert_message
from websiteapp.contactapp.models import get_all_contact_items
from websiteapp.contactapp.forms import ContactForm


def contact(request):
    """ return the page with contact form
    save a message and send email"""
    # Page contact
    page = get_page("contact")
    # Contact items
    contact_items = get_all_contact_items()
    # contact_items = ContactItem.objects.all().order_by('position')
    # Main titles
    main_titles = get_page("main-contact")
    # Card buttons
    buttons_card = get_buttons_card("contact")
    # Form POST
    form = ContactForm()
    sent_message = False
    if request.method == 'POST':
        # message has sent
        form = ContactForm(request.POST, )
        if form.is_valid():
            # send the message to admin and save it in db
            message = form.save(commit=False)
            send_mail(
                message.subject, message.content,
                "DjangoWebSite: {} <- {} ->".format(
                    message.contact_name, message.contact_email),
                ['JBthePenguin'], fail_silently=False)
            message.save()
            form = ContactForm()
            # Alert messages
            sent_message = get_alert_message("sent message")
    context = Context()
    context.update(
        page=page, contact_items=contact_items,
        main_titles=main_titles, btn_card_text=buttons_card[0].text,
        sent_message=sent_message, form=form)
    return render(request, 'contactapp/contact.html', context)
